from PyQt5 import QtWidgets

from kuberider.entities.model import KubePodItem
from ..generated.pod_item_widget import Ui_PodItemWidget


class PodItemWidget(QtWidgets.QWidget, Ui_PodItemWidget):

    def __init__(self, pod_info: KubePodItem, parent=None):
        super(PodItemWidget, self).__init__(parent)
        self.setupUi(self)
        self.pod_info = pod_info
        self.set_data(pod_info)

    def set_data(self, pod_info: KubePodItem):
        self.lbl_pod_name.setText(pod_info.name)
        self.lbl_pod_count.setText(pod_info.count)
        self.lbl_pod_status.setText(pod_info.pod_status)

    def get_data(self):
        return self.pod_info
