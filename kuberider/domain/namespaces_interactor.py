from kuberider.domain.interactor import Interactor
from kuberider.entities.model import KubeNamespaces
from kuberider.settings.app_settings import app


class NamespacesLoaderInteractor(Interactor):
    def __init__(self):
        super().__init__(
            on_success=self.on_result, on_failure=self.on_failure
        )

    def load_namespaces(self):
        self.kcb.ctx().command(f"get namespaces -o json").start()

    def on_result(self, result):
        output = result['output']
        kube_namespaces = KubeNamespaces.from_json_str(output)
        namespaces = [i.metadata.get('name') for i in kube_namespaces.items]
        app.data.save_namespaces(namespaces)
        app.data.signals.namespaces_loaded.emit()

    def on_failure(self, result):
        app.data.save_namespaces([])
        app.data.signals.namespaces_loaded.emit()


class ChangeNamespaceInteractor(Interactor):
    def update_namespace(self, namespace):
        app.data.update_current_namespace(namespace)
        app.data.signals.namespace_changed.emit()
