import json
from typing import List, Dict, Any

import attr
import cattr

APP_STATE_RECORD_TYPE = "app_state"


@attr.s(auto_attribs=True)
class AppState:
    record_type: str = APP_STATE_RECORD_TYPE
    contexts: List[str] = []
    commands: List[str] = []
    current_context: str = None
    namespaces: List[str] = []
    current_namespace: str = None

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
    def count(self):
        total = len([c for c in self.status.get('containerStatuses', [])])
        ready = len([
            c
            for c in self.status.get('containerStatuses', [])
            if c.get('ready')
        ])
        return f"{ready}/{total}"

    @property
    def pod_status(self):
        return self.status.get('phase')


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
#     mock_file = Path("..").joinpath("mock_responses").joinpath("k_get_qa_default_pods.json").read_text(encoding='utf-8')
#     pods = KubePods.from_json_str(mock_file)
