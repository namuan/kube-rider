from PyQt5 import QtWidgets

from ..entities.model import KubePodContainer, KubePodItem
from ..generated.pod_container_widget import Ui_PodContainerWidget
from ..settings.app_settings import app


class PodContainerWidget(QtWidgets.QWidget, Ui_PodContainerWidget):
    pod_info: KubePodItem
    pod_container: KubePodContainer

    def __init__(self, pod_info: KubePodItem, pod_container: KubePodContainer, parent=None):
        super(PodContainerWidget, self).__init__(parent)
        self.setupUi(self)
        self.pod_info = pod_info
        self.set_data(pod_container)

        # ui events
        self.btn_open_logs.clicked.connect(self.on_open_logs)
        self.btn_exec_shell.clicked.connect(self.on_exec_shell)
        self.btn_port_forward.clicked.connect(self.on_port_forward)
        self.btn_follow_logs.clicked.connect(self.on_follow_logs)

    def set_data(self, pod_container: KubePodContainer):
        self.pod_container = pod_container
        self.lbl_container_name.setText(pod_container.name)
        self.lbl_container_status.setAccessibleName(pod_container.state)
        self.lbl_container_status.setText(pod_container.state_details)
        self.lbl_container_image.setText(pod_container.image)
        self.lbl_volumes.setText(",".join(pod_container.volumeMounts.keys()))
        self.lbl_volumes.setToolTip(",".join(pod_container.volumeMounts.values()))

    def get_data(self):
        return self.pod_info

    def on_open_logs(self):
        app.commands.open_pod_logs.emit(self.pod_info.name, self.pod_container.name)

    def on_exec_shell(self):
        app.commands.on_exec_shell.emit(self.pod_info.name, self.pod_container.name)

    def on_port_forward(self):
        app.commands.on_port_forward.emit(self.pod_info.name, self.pod_container.name)

    def on_follow_logs(self):
        app.commands.on_follow_logs.emit(self.pod_info.name, self.pod_container.name)