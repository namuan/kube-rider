import json
import warnings
from typing import List, Dict, Any, Optional

import arrow
import attr
import cattr
from arrow.factory import ArrowParseWarning
from toolz import itertoolz

warnings.simplefilter("ignore", ArrowParseWarning)

APP_STATE_RECORD_TYPE = "app_state"


@attr.s(auto_attribs=True)
class AppState:
    record_type: str = APP_STATE_RECORD_TYPE
    contexts: List[str] = []
    commands: List[str] = []
    current_context: str = None
    namespaces: List[str] = []
    current_namespace: str = None
    pods_filter: str = None

    @classmethod
    def from_json(cls, json_obj):
        if not json_obj:
            return cls()
        return cattr.structure(json_obj, cls)

    def to_json(self):
        return cattr.unstructure(self)

    def to_json_str(self):
        return json.dumps(self.to_json())


@attr.s(auto_attribs=True)
class KubeNamespace(object):
    apiVersion: str
    kind: str
    metadata: Dict = {}
    spec: Dict = {}
    status: Dict = {}


@attr.s(auto_attribs=True)
class KubeNamespaces(object):
    apiVersion: str
    kind: str
    metadata: Dict
    items: List[KubeNamespace]

    @classmethod
    def from_json_str(cls, json_str):
        return cattr.structure(json.loads(json_str), cls)


@attr.s(auto_attribs=True)
class KubePodContainer(object):
    name: str
    image: str
    volumeMounts: Dict
    ready: bool
    container_id: str
    restart_count: Optional[int]
    state: str
    state_details: str

    @staticmethod
    def extract_container_state(state_json):
        if not state_json:
            return "N/A"

        current_state = itertoolz.first(state_json)
        current_state_details = state_json.get(current_state)
        state_at = itertoolz.first(current_state_details)
        state_at_details = current_state_details.get(state_at)
        if state_at == "startedAt":
            state_at_details = arrow.get(state_at_details).humanize()

        return current_state, f"{current_state.strip()} ({state_at.strip()}: {state_at_details.strip()})"

    @classmethod
    def from_spec(cls, json_spec, json_container_status):
        container_name = json_spec.get('name', None)
        container_status = next(cs
                                for cs in json_container_status.get('containerStatuses')
                                if cs.get('name') == container_name
                                )
        state, details = cls.extract_container_state(container_status.get('state'))

        return cls(
            name=json_spec.get('name', None),
            image=json_spec.get('image', None),
            ready=container_status.get('ready', False),
            container_id=container_status.get('containerID', None),
            restart_count=container_status.get('restartCount', None),
            volumeMounts={
                vol.get('name'): vol.get('mountPath')
                for vol in json_spec.get('volumeMounts', [])
            },
            state=state,
            state_details=details
        )


@attr.s(auto_attribs=True)
class KubePodItem(object):
    apiVersion: str
    kind: Any
    metadata: Dict
    spec: Dict
    status: Dict

    @property
    def name(self):
        return self.metadata.get('name')

    @property
    def pod_state(self):
        ready, total = self.count
        return "running" if ready == total else "waiting"

    @property
    def count(self):
        total = len([c for c in self.status.get('containerStatuses', [])])
        ready = len([
            c
            for c in self.status.get('containerStatuses', [])
            if c.get('ready')
        ])
        return ready, total

    @property
    def pod_status(self):
        return self.status.get('phase')

    @property
    def containers(self):
        return [
            KubePodContainer.from_spec(container_spec, self.status)
            for container_spec in self.spec.get('containers', [])
        ]

    @property
    def volumes(self):
        return []


@attr.s(auto_attribs=True)
class KubePodEvents(object):
    apiVersion: str
    kind: Any
    metadata: Any
    items: List[Dict]

    @classmethod
    def from_json_str(cls, json_str):
        return cattr.structure(json.loads(json_str), cls)


@attr.s(auto_attribs=True)
class KubePods(object):
    apiVersion: str
    items: List[KubePodItem]
    kind: Any
    metadata: Any

    @classmethod
    def from_json_str(cls, json_str):
        return cattr.structure(json.loads(json_str), cls)

# if __name__ == '__main__':
#     mock_file = Path("..").joinpath("mock_responses").joinpath("k_get_qa_multiple_pods.json").read_text(
#         encoding='utf-8')
#     pods = KubePods.from_json_str(mock_file)
#     for p in pods.items:
#         for c in p.containers:
#             print(c.name, c.state)
