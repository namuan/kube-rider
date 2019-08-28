from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


def toolbar_items(self):
    """Create a tool bar for the main window."""
    self.toolbar.setObjectName("maintoolbar")
    self.addToolBar(Qt.TopToolBarArea, self.toolbar)
    self.toolbar.setMovable(False)

    toolbar_configure_action = QAction(QIcon(":/images/configure-48.png"), 'Settings', self)
    toolbar_configure_action.triggered.connect(self.configuration_dialog.show_dialog)
    self.toolbar.addAction(toolbar_configure_action)

    toolbar_add_resource_action = QAction(QIcon(":/images/plus-48.png"), 'Add Resource', self)
    toolbar_add_resource_action.triggered.connect(self.kube_resource_presenter.show_dialog)
    self.toolbar.addAction(toolbar_add_resource_action)

    self.toolbar.addSeparator()

    toolbar_load_contexts_action = QAction(QIcon(":/images/load-contexts-48.png"), 'Load Contexts', self)
    toolbar_load_contexts_action.triggered.connect(self.toolbar_presenter.on_toolbar_load_contexts)
    self.toolbar.addAction(toolbar_load_contexts_action)

    toolbar_ctx_list = QComboBox(self)
    toolbar_ctx_list.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
    toolbar_ctx_list.setDuplicatesEnabled(False)
    toolbar_ctx_list.currentIndexChanged[str].connect(
        lambda new_ctx: self.toolbar_presenter.on_current_context_changed(new_ctx)
    )
    toolbar_ctx_list_action = QWidgetAction(self)
    toolbar_ctx_list_action.setText("Contexts")
    toolbar_ctx_list_action.setDefaultWidget(toolbar_ctx_list)
    self.toolbar.addAction(toolbar_ctx_list_action)

    toolbar_ns_list = QComboBox(self)
    toolbar_ns_list.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
    toolbar_ns_list.setDuplicatesEnabled(False)
    toolbar_ns_list.currentIndexChanged[str].connect(
        lambda new_ns: self.toolbar_presenter.on_current_namespace_changed(new_ns)
    )
    toolbar_ns_list.setEditable(True)
    toolbar_ns_list_action = QWidgetAction(self)
    toolbar_ns_list_action.setText("Namespaces")
    toolbar_ns_list_action.setDefaultWidget(toolbar_ns_list)
    self.toolbar.addAction(toolbar_ns_list_action)

    spacer = QWidget(self)
    spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.toolbar.addWidget(spacer)

    toolbar_update_available = QAction(QIcon(":/images/download-disabled-48.png"), 'Update Available', self)
    toolbar_update_available.setEnabled(False)
    toolbar_update_available.triggered.connect(self.open_releases_page)

    self.toolbar.addAction(toolbar_update_available)
