import logging
from typing import Optional, List

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QAbstractItemModel, QModelIndex
from PyQt5.QtWidgets import QAction, QMenu, QMessageBox

from kuberider.domain.pods_interactor import GetPodsInteractor, DeletePodInteractor
from kuberider.entities.model import KubePodItem
from kuberider.settings.app_settings import app
from kuberider.widgets.pod_item_widget import PodItemWidget


class PodListPresenter:
    def __init__(self, parent_view=None):
        self.view = parent_view
        self.get_pods = GetPodsInteractor()
        self.delete_pod = DeletePodInteractor()

        # context menu
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.view.customContextMenuRequested.connect(self.show_context_menu)

        # Context Menu setup
        remove_action = QAction("Delete", self.view)
        remove_action.triggered.connect(self.on_remove_selected_item)

        self.menu = QMenu()
        self.menu.addAction(remove_action)

        # ui events
        self.view.clicked.connect(self.ui_pod_selected)

        # domain events
        app.data.signals.namespace_changed.connect(self.on_namespace_changed)
        app.data.signals.pods_loaded.connect(self.on_pods_loaded)
        app.data.signals.pod_deleted.connect(self.get_all_pods)
        app.data.signals.filter_enabled.connect(self.on_namespace_changed)
        app.data.signals.filter_cleared.connect(self.on_namespace_changed)
        app.commands.reload_pods.connect(self.get_all_pods)

    def ui_pod_selected(self):
        pod_item: KubePodItem = self.currently_selected_pod()
        logging.info(f"Selected {pod_item}")
        app.data.signals.pod_selected.emit(pod_item)

    def on_namespace_changed(self):
        self.get_all_pods()

    def get_all_pods(self):
        self.view.clear()
        self.get_pods.run()

    def currently_selected_pod(self) -> Optional[KubePodItem]:
        selected_items = self.view.selectedItems()
        if selected_items:
            item = self.view.itemWidget(self.view.selectedItems()[0])
            return item.get_data()

    def on_pods_loaded(self, pods: List[KubePodItem]):
        logging.info(f"on_pods_loaded: Displaying {len(pods)}")
        pod_item = self.currently_selected_pod()

        for pod in pods:
            self.add_or_update_pod_item(pod)

        if pod_item:
            existing_pod_index = self.find_pod_index_by_name(pod_item.name)
            if existing_pod_index:
                item_widget = self.view.item(existing_pod_index.row())
                self.view.setCurrentItem(item_widget)

    def find_pod_index_by_name(self, pod_name):
        m: QAbstractItemModel = self.view.model()
        items = m.match(m.index(0, 0), Qt.UserRole, pod_name, 1, Qt.MatchExactly)
        return items[0] if items else None

    def add_or_update_pod_item(self, pod_info: KubePodItem):
        current_filter = app.data.app_state.pods_filter
        if current_filter and current_filter not in pod_info.name:
            return

        existing_pod_index = self.find_pod_index_by_name(pod_info.name)

        if existing_pod_index:
            item_row = existing_pod_index.row()
            existing_pod_info = self.pod_at_row(item_row)
            if self.pod_changed(existing_pod_info, pod_info):
                self.view.takeItem(item_row)
                pod_widget = PodItemWidget(pod_info, self.view)
                pod_widget_item = QtWidgets.QListWidgetItem(self.view)
                pod_widget_item.setData(Qt.UserRole, pod_info.name)
                pod_widget_item.setSizeHint(pod_widget.sizeHint())
                self.view.insertItem(item_row, pod_widget_item)
                self.view.setItemWidget(pod_widget_item, pod_widget)
        else:
            pod_widget = PodItemWidget(pod_info, self.view)
            pod_widget_item = QtWidgets.QListWidgetItem(self.view)
            pod_widget_item.setData(Qt.UserRole, pod_info.name)
            pod_widget_item.setSizeHint(pod_widget.sizeHint())
            self.view.addItem(pod_widget_item)
            self.view.setItemWidget(pod_widget_item, pod_widget)

    def pod_changed(self, old, new):
        is_changed = old.name != new.name or old.pod_status != new.pod_status
        return is_changed

    def pod_at_row(self, item_row):
        item_widget = self.view.item(item_row)
        pod_widget: PodItemWidget = self.view.itemWidget(item_widget)
        return pod_widget.get_data()

    def show_context_menu(self, position):
        index: QModelIndex = self.view.indexAt(position)
        if not index.isValid():
            return

        global_position = self.view.viewport().mapToGlobal(position)
        self.menu.exec_(global_position)

    def on_remove_selected_item(self):
        pod_item = self.currently_selected_pod()
        app_state = app.data.app_state
        msg_box = QMessageBox(
            QMessageBox.Warning,
            "Confirmation",
            f"Selected context {app_state.current_context} and namespace {app_state.current_namespace}\nDelete {pod_item.name}?",
            QMessageBox.Ok | QMessageBox.Cancel
        )
        msg_box.setDefaultButton(QMessageBox.Ok)
        if msg_box.exec_() == QMessageBox.Ok:
            self.delete_pod.delete(pod_item.name)
