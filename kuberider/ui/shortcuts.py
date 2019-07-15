from PyQt5.QtGui import *
from PyQt5.QtWidgets import QShortcut


def shortcut_items(self):
    http_url = QShortcut(QKeySequence("Ctrl+L"), self)
    http_url.activated.connect(self.empty_frame_presenter.test_shortcut)
    # http_url.activated.connect(self.progress_dialog.show_dialog)
