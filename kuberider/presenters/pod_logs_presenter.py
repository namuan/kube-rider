import logging

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

    def on_open_logs_dialog(self, pod_name, container_name):
        self.pod_logs_dialog.show_dialog()
        self.pods_logs.tail(pod_name, container_name)

        # update the dialog box as we receive more data

    def on_close_logs_dialog(self):
        self.pod_logs_dialog.hide_dialog()
        # close the thread
        # close dialog box
