import logging
from typing import Optional, List

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QAbstractItemModel

from kuberider.domain.pods_interactor import GetPodsInteractor
from kuberider.entities.model import KubePodItem
from kuberider.settings.app_settings import app
from kuberider.widgets.pod_item_widget import PodItemWidget


class PodListPresenter:
    def __init__(self, parent_view=None):
        self.view = parent_view
        self.get_pods = GetPodsInteractor()

        # ui events
        self.view.clicked.connect(self.ui_pod_selected)

        # domain events
        app.data.signals.namespace_changed.connect(self.on_namespace_changed)
        app.data.signals.pods_loaded.connect(self.on_pods_loaded)
        app.commands.reload_pods.connect(self.get_all_pods)
        app.commands.update_pods.connect(self.update_pending_pod)
        app.commands.log_pods.connect(self.log_all_pods)

    def ui_pod_selected(self):
        pod_item: KubePodItem = self.currently_selected_pod()
        logging.info(f"Selected {pod_item}")

    def on_namespace_changed(self, namespace):
        self.get_all_pods()

    def get_all_pods(self):
        self.get_pods.run()

    def currently_selected_pod(self) -> Optional[KubePodItem]:
        selected_items = self.view.selectedItems()
        if selected_items:
            item = self.view.itemWidget(self.view.selectedItems()[0])
            return item.get_data()
        else:
            None

    def on_pods_loaded(self, pods: List[KubePodItem]):
        logging.info(f"on_pods_loaded: Displaying {len(pods)}")
        pod_item = self.currently_selected_pod()

        self.view.clear()
        for pod in pods:
            self.add_or_update_pod_item(pod)

        if pod_item:
            logging.info(f"Re-Select {pod_item} in list")

    def add_or_update_pod_item(self, pod_info: KubePodItem):
        pod_widget = PodItemWidget(pod_info, self.view)
        pod_widget_item = QtWidgets.QListWidgetItem(self.view)
        pod_widget_item.setData(Qt.UserRole, pod_info.name)
        pod_widget_item.setSizeHint(pod_widget.sizeHint())

        m: QAbstractItemModel = self.view.model()
        items = m.match(m.index(0, 0), Qt.UserRole, pod_info.name, 1, Qt.MatchExactly)
        if items:
            item_row = items[0].row()
            self.view.takeItem(item_row)
            self.view.insertItem(item_row, pod_widget_item)
        else:
            self.view.addItem(pod_widget_item)

        self.view.setItemWidget(pod_widget_item, pod_widget)

    def update_pending_pod(self):
        pod_to_update = "hello-node-64c578bdf8-mwpff"
        changed_pod: KubePodItem = KubePodItem(
            apiVersion="",
            kind=None,
            metadata={},
            spec={},
            status={}
        )
        changed_pod.metadata['name'] = pod_to_update
        changed_pod.status['phase'] = 'Completed'
        self.add_or_update_pod_item(changed_pod)

    def log_all_pods(self):
        for ic in range(self.view.count()):
            item_widget = self.view.item(ic)
            pod_widget = self.view.itemWidget(item_widget)
            pod_info = pod_widget.get_data()
            logging.info(f"{pod_info.name} -> {pod_info.pod_status}")
