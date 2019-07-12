from PyQt5.QtWidgets import (QAction, QMenu)


def menu_items(self):
    # File Menu
    new_action = QAction('&New', self)
    new_action.setShortcut('Ctrl+N')
    new_action.triggered.connect(self.file_menu_presenter.on_file_new)

    f: QMenu = self.menu_bar.addMenu("&File")
    f.addAction(new_action)
