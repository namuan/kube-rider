from typing import List

from kuberider.domain.pods_interactor import GetPodEventsInteractor
from kuberider.entities.model import KubePodItem
from kuberider.settings.app_settings import app


class PodEventsPresenter:
    def __init__(self, view):
        self.view = view
        self.pod_events = GetPodEventsInteractor()

        # domain events
        app.data.signals.pod_selected.connect(self.on_pod_selected)
        app.data.signals.pod_events_loaded.connect(self.on_pod_events_loaded)

    def on_pod_selected(self, pod_info: KubePodItem):
        self.pod_events.run(pod_info.name)
        pass

    def on_pod_events_loaded(self, pod_events: List):
        self.view.clear()
        for event in pod_events:
            self.view.appendPlainText(event.get("message"))
