import logging

from kuberider.core.kube_command_builder import Kcb
from kuberider.core.worker_pool import TailCommandThread
from kuberider.domain.interactor import Interactor
from kuberider.entities.model import KubePods, KubePodEvents
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


class PodLogsInteractor(Interactor):
    def __init__(self):
        super().__init__(on_success=self.on_full_logs, on_failure=self.on_full_logs)
        self.tct = TailCommandThread()
        self.ct.signals.partial_output.connect(self.on_partial_output)

    def on_partial_output(self, output):
        logging.debug(f"Read: {output}")
        app.data.save_partial_output(output)

    def on_full_logs(self, result):
        app.data.signals.command_finished.emit()
        output = result['output']
        app.data.save_partial_output(output)

    def fetch_all(self, pod_name, container_name):
        app.data.signals.command_started.emit("Getting all logs", False)
        self.kcb = Kcb.init(self.ct)
        logging.info(f"Fetching all logs for {pod_name} -> {container_name}")
        command = f'logs {pod_name} -c {container_name}'
        self.kcb.ctx().ns().command(command).start()

    def tail(self, pod_name, container_name):
        self.kcb = Kcb.init(self.tct)
        logging.info(f"Following logs for {pod_name} -> {container_name}")
        command = f'logs {pod_name} -c {container_name} -f'
        self.kcb.ctx().ns().command(command).start()

    def stop_tail(self):
        self.tct.stop_process()


class GetPodEventsInteractor(Interactor):
    def __init__(self):
        super().__init__(on_success=self.on_result, on_failure=self.on_result)

    def run(self, pod_name):
        app.data.signals.command_started.emit("Getting pod events", False)
        event_query = f"--field-selector='involvedObject.name={pod_name}'"
        self.kcb.ctx().ns().command(f"get event {event_query} -o json").start()

    def on_result(self, result):
        app.data.signals.command_finished.emit()
        output = result['output']
        kube_pod_events = KubePodEvents.from_json_str(output)
        app.data.save_pod_events(kube_pod_events.items)
