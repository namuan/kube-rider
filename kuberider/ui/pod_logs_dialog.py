from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import (QDialog)

from ..generated.pod_logs_dialog import Ui_PodLogsDialog


class PodLogsDialog(QDialog, Ui_PodLogsDialog):

    def __init__(self, parent=None):
        super(PodLogsDialog, self).__init__(parent)
        self.initialize()

    def initialize(self):
        self.setupUi(self)

    def hide_dialog(self):
        self.hide()

    def show_dialog(self):
        self.show()

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() != Qt.Key_Escape:
            super(QDialog, self).keyPressEvent(e)
