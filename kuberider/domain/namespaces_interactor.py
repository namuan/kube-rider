from kuberider.core.kube_command_builder import Kcb
from kuberider.core.worker_pool import CommandThread
from kuberider.entities.model import KubeNamespaces
from kuberider.settings.app_settings import app


class NamespacesLoaderInteractor:
    def __init__(self):
        self.ct = CommandThread()

    def load_namespaces(self):
        Kcb.init().ctx().command(f"get namespaces -o json").start(
            self.ct,
            on_success=self.on_result,
            on_failure=self.on_result
        )

    def on_result(self, result):
        output = result['output']
        kube_namespaces = KubeNamespaces.from_json_str(output)
        namespaces = [i.metadata.get('name') for i in kube_namespaces.items]
        app.data.save_namespaces(namespaces)
        app.data.signals.namespaces_loaded.emit()


class CurrentNamespaceInteractor:
    def __init__(self):
        self.ct = CommandThread()

    def current_namespace(self):
        Kcb.init().ctx().command(f"config current-namespace").start(
            self.ct,
            on_success=self.on_result,
            on_failure=self.on_result
        )

    def on_result(self, result):
        output = result['output']
        app.data.update_current_namespace(output)
        app.data.signals.namespace_changed.emit(output)
