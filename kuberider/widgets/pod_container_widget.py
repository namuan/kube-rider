from PyQt5 import QtWidgets

from ..entities.model import KubePodContainer
from ..generated.pod_container_widget import Ui_PodContainerWidget


class PodContainerWidget(QtWidgets.QWidget, Ui_PodContainerWidget):
    pod_container: KubePodContainer

    def __init__(self, pod_container: KubePodContainer, parent=None):
        super(PodContainerWidget, self).__init__(parent)
        self.setupUi(self)
        self.set_data(pod_container)

    def set_data(self, pod_container: KubePodContainer):
        self.pod_container = pod_container
        self.lbl_container_name.setText(pod_container.name)
        self.lbl_container_started.setText(f"Started at: {pod_container.start_time}")
        self.lbl_container_image.setText(pod_container.image)
        self.lbl_volumes.setText(",".join(pod_container.volumeMounts.keys()))
        self.lbl_volumes.setToolTip(",".join(pod_container.volumeMounts.values()))

    def get_data(self):
        return self.pod_info
