from PyQt5.QtGui import *
from PyQt5.QtWidgets import QShortcut


def shortcut_items(self):
    short = QShortcut(QKeySequence("Ctrl+L"), self)
    # short.activated.connect(self.progress_dialog.show_dialog)
    pass
