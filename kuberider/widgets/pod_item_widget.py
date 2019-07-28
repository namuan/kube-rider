from PyQt5 import QtWidgets

from ..entities.model import KubePodItem
from ..generated.pod_item_widget import Ui_PodItemWidget


class PodItemWidget(QtWidgets.QWidget, Ui_PodItemWidget):
    pod_info: KubePodItem

    def __init__(self, pod_info: KubePodItem, parent=None):
        super(PodItemWidget, self).__init__(parent)
        self.setupUi(self)
        self.set_data(pod_info)

    def set_data(self, pod_info: KubePodItem):
        self.pod_info = pod_info
        self.lbl_pod_name.setText(pod_info.name)
        self.lbl_pod_count.setText(pod_info.count)
        self.lbl_pod_status.setText(pod_info.pod_status)

    def get_data(self):
        return self.pod_info
