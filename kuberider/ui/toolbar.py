from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


def tool_bar_items(self):
    """Create a tool bar for the main window."""
    self.tool_bar.setObjectName("maintoolbar")
    self.addToolBar(Qt.TopToolBarArea, self.tool_bar)
    self.tool_bar.setMovable(False)

    tool_bar_configure_action = QAction(QIcon(":/images/configure-48.png"), 'Settings', self)
    tool_bar_configure_action.triggered.connect(self.configuration_dialog.show_dialog)
    self.tool_bar.addAction(tool_bar_configure_action)

    self.tool_bar.addSeparator()

    tool_bar_ctx_list = QComboBox(self)
    tool_bar_ctx_list.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
    tool_bar_ctx_list.setDuplicatesEnabled(False)
    tool_bar_ctx_list.currentTextChanged.connect(lambda x: x)
    tool_bar_ctx_list_action = QWidgetAction(self)
    tool_bar_ctx_list_action.setText("Contexts")
    tool_bar_ctx_list_action.setDefaultWidget(tool_bar_ctx_list)
    self.tool_bar.addAction(tool_bar_ctx_list_action)

    self.tool_bar.addSeparator()

    tool_bar_ns_list = QComboBox(self)
    tool_bar_ns_list.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
    tool_bar_ns_list.setDuplicatesEnabled(False)
    tool_bar_ns_list.currentTextChanged.connect(lambda x: x)
    tool_bar_ns_list_action = QWidgetAction(self)
    tool_bar_ns_list_action.setText("Namespaces")
    tool_bar_ns_list_action.setDefaultWidget(tool_bar_ns_list)
    self.tool_bar.addAction(tool_bar_ns_list_action)

    spacer = QWidget(self)
    spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.tool_bar.addWidget(spacer)

    tool_bar_update_available = QAction(QIcon(":/images/download-disabled-48.png"), 'Update Available', self)
    tool_bar_update_available.setEnabled(False)
    tool_bar_update_available.triggered.connect(self.open_releases_page)

    self.tool_bar.addAction(tool_bar_update_available)
