from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import (QDialog)

from kuberider.settings.app_settings import app
from ..generated.progress_dialog import Ui_ProgressDialog


class ProgressDialog(QDialog, Ui_ProgressDialog):

    def __init__(self, parent=None):
        super(ProgressDialog, self).__init__(parent)
        self.initialize()
        self.btn_cancel_progress.pressed.connect(self.cancel_processing)
        app.data.signals.command_started.connect(self.show_dialog)
        app.data.signals.command_finished.connect(self.hide_dialog)

    def initialize(self):
        self.setupUi(self)
        self.setFixedSize(self.size())

    def cancel_processing(self):
        self.update_status("Cancelling....")

    def show_dialog(self, message=""):
        self.lbl_progress_status.setText(message)
        self.show()

    def hide_dialog(self):
        self.lbl_progress_status.setText("")
        self.hide()

    def update_status(self, message):
        self.lbl_progress_status.setText(message)

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() != Qt.Key_Escape:
            super(QDialog, self).keyPressEvent(e)
