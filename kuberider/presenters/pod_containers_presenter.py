import logging

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from kuberider.entities.model import KubePodItem
from kuberider.settings.app_settings import app
from kuberider.widgets.pod_container_widget import PodContainerWidget


class PodContainersPresenter:
    def __init__(self, view):
        self.view = view

        # domain events
        app.data.signals.pod_selected.connect(self.on_pod_selected)

    def on_pod_selected(self, pod_info: KubePodItem):
        self.view.clear()
        for container in pod_info.containers:
            pod_container_widget = PodContainerWidget(pod_info, container, self.view)
            pod_container_widget_item = QtWidgets.QListWidgetItem(self.view)
            pod_container_widget_item.setData(Qt.UserRole, container.name)
            pod_container_widget_item.setSizeHint(pod_container_widget.sizeHint())

            self.view.addItem(pod_container_widget_item)
            self.view.setItemWidget(pod_container_widget_item, pod_container_widget)
