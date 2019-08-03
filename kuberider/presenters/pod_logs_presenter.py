from kuberider.domain.pods_interactor import PodLogsInteractor
from kuberider.settings.app_settings import app
from kuberider.ui.pod_logs_dialog import PodLogsDialog


class PodLogsPresenter:
    def __init__(self, parent):
        self.parent = parent
        self.pod_logs_dialog = PodLogsDialog(self.parent)
        self.pods_logs = PodLogsInteractor()

        # ui events
        self.pod_logs_dialog.btn_close_logs.pressed.connect(self.on_close_logs_dialog)

        # domain event
        app.commands.open_pod_logs.connect(self.on_open_logs_dialog)
        app.data.signals.output_generated.connect(self.on_output_generated)

    def on_open_logs_dialog(self, pod_name, container_name):
        self.pod_logs_dialog.show_dialog()
        self.pod_logs_dialog.txt_pod_logs.clear()
        self.pods_logs.tail(pod_name, container_name)

    def on_close_logs_dialog(self):
        self.pods_logs.stop_tail()
        self.pod_logs_dialog.hide_dialog()

    def on_output_generated(self, output):
        self.pod_logs_dialog.txt_pod_logs.appendPlainText(output)
