from kuberider.core.kube_command_builder import Kcb
from kuberider.core.worker_pool import CommandThread
from kuberider.settings.app_settings import app


class NamespacesLoaderInteractor:
    def __init__(self):
        self.ct = CommandThread()

    def load_namespaces(self):
        Kcb.init().ctx().command(f"get namespaces").start(
            self.ct,
            on_success=self.on_result,
            on_failure=self.on_result
        )

    def on_result(self, result):
        output = result['output']
        namespaces = []
        # contexts = output.splitlines()
        app.data.save_namespaces(namespaces)


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
