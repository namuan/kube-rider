import logging

from kuberider.core.kube_command_builder import Kcb
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
        self.kcb = Kcb.init(self.ct)
        self.ct.signals.partial_output.connect(self.on_partial_output)

    def on_partial_output(self, output):
        logging.debug(f"Read: {output}")
        app.data.save_partial_output(output)

    def tail(self, pod_name, container_name):
        logging.info(f"Opening logs for {pod_name} -> {container_name}")
        self.ct.command = 'tail -f $HOME/d.txt'
        self.kcb.ctx().ns().command("get logs").start()

    def stop_tail(self):
        self.ct.stop_process()
