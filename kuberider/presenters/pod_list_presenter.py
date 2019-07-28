import logging

from PyQt5 import QtWidgets

from kuberider.domain.pods_interactor import GetPodsInteractor
from kuberider.settings.app_settings import app
from kuberider.widgets.pod_item_widget import PodItemWidget


class PodListPresenter:
    def __init__(self, parent_view=None):
        self.view = parent_view
        self.get_pods = GetPodsInteractor()

        # events
        app.data.signals.namespace_changed.connect(self.on_namespace_changed)
        app.data.signals.pods_loaded.connect(self.on_pods_loaded)

    def on_namespace_changed(self, namespace):
        self.get_pods.run()

    def on_pods_loaded(self, pods):
        logging.info(f"on_pods_loaded: Displaying {len(pods)}")
        self.view.clear()
        for pod in pods:
            pod_widget = PodItemWidget(pod, self.view)
            pod_widget_item = QtWidgets.QListWidgetItem(self.view)
            pod_widget_item.setSizeHint(pod_widget.sizeHint())

            self.view.addItem(pod_widget_item)
            self.view.setItemWidget(pod_widget_item, pod_widget)
