import logging
from typing import Optional

from PyQt5 import QtWidgets

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

    def on_pods_loaded(self, pods):
        logging.info(f"on_pods_loaded: Displaying {len(pods)}")
        pod_item = self.currently_selected_pod()

        self.view.clear()
        for pod in pods:
            pod_widget = PodItemWidget(pod, self.view)
            pod_widget_item = QtWidgets.QListWidgetItem(self.view)
            pod_widget_item.setSizeHint(pod_widget.sizeHint())

            self.view.addItem(pod_widget_item)
            self.view.setItemWidget(pod_widget_item, pod_widget)

        if pod_item:
            logging.info(f"Re-Select {pod_item} in list")
