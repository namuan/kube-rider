from PyQt5.QtWidgets import (QDialog)

from ..generated.kube_resource_dialog import Ui_KubeResourceDialog


class KubeResourceDialog(QDialog, Ui_KubeResourceDialog):

    def __init__(self, parent=None):
        super(KubeResourceDialog, self).__init__(parent)
        self.setupUi(self)
