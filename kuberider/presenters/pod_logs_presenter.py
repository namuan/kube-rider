from typing import Optional

from PyQt5.QtCore import Qt

from ..domain.pods_interactor import PodLogsInteractor
from ..settings.app_settings import app
from ..ui.pod_logs_dialog import PodLogsDialog


class PodLogsPresenter:
    pod_name: Optional[str] = None
    container_name: Optional[str] = None

    def __init__(self, parent):
        self.parent = parent
        self.pod_logs_dialog = PodLogsDialog(self.parent)
        self.pods_logs = PodLogsInteractor()

        # ui events
        self.pod_logs_dialog.btn_close_logs.pressed.connect(self.on_close_logs_dialog)
        self.pod_logs_dialog.chk_follow_logs.stateChanged.connect(self.follow_logs)

        # domain event
        app.commands.open_pod_logs.connect(self.on_open_logs_dialog)
        app.data.signals.output_generated.connect(self.on_output_generated)

    def on_open_logs_dialog(self, pod_name, container_name):
        self.pod_name = pod_name
        self.container_name = container_name

        self.pod_logs_dialog.show_dialog()
        self.start_tailing()

    def on_close_logs_dialog(self):
        self.pod_name = None
        self.container_name = None
        self.pods_logs.stop_tail()
        self.pod_logs_dialog.hide_dialog()

    def on_output_generated(self, output):
        self.pod_logs_dialog.txt_pod_logs.appendPlainText(output)

    def follow_logs(self, state):
        if state == Qt.Checked:
            self.pods_logs.stop_tail()
            self.start_tailing()

    def start_tailing(self):
        follow_logs = self.pod_logs_dialog.chk_follow_logs.isChecked()
        self.pod_logs_dialog.txt_pod_logs.clear()
        self.pods_logs.tail(self.pod_name, self.container_name, follow=follow_logs)
