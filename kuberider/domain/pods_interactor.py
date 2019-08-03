import logging

from kuberider.core.worker_pool import TailCommandThread
from kuberider.domain.interactor import Interactor
from kuberider.entities.model import KubePods
from kuberider.settings.app_settings import app


class GetPodsInteractor(Interactor):
    def __init__(self):
        super().__init__(on_success=self.on_result, on_failure=self.on_result)

    def run(self):
        app.data.signals.command_started.emit("Getting all pods", False)
        self.kcb.ctx().ns().command("get pods -o json").start()

    def on_result(self, result):
        app.data.signals.command_finished.emit()
        output = result['output']
        kube_pods: KubePods = KubePods.from_json_str(output)
        app.data.save_pods(kube_pods.items)

    def apply_filter(self, filter):
        app.data.save_filter(filter)
        app.data.signals.filter_enabled.emit()

    def clear_filter(self):
        app.data.save_filter(None)
        app.data.signals.filter_cleared.emit()


class FilterPodsInteractor:
    def apply_filter(self, filter):
        app.data.save_filter(filter)
        app.data.signals.filter_enabled.emit()

    def clear_filter(self):
        app.data.save_filter(None)
        app.data.signals.filter_cleared.emit()


class PodLogsInteractor:
    def __init__(self):
        self.ct = TailCommandThread()
        self.ct.signals.success.connect(self.on_success)
        self.ct.signals.failure.connect(self.on_failure)

    def on_success(self):
        pass

    def on_failure(self):
        pass

    def tail(self, pod_name, container_name):
        logging.info(f"Opening logs for {pod_name} -> {container_name}")
        # start a thread to read data from tail command
        pass
