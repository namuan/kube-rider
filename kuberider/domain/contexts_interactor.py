from kuberider.core.kube_command_builder import Kcb
from kuberider.core.worker_pool import CommandThread
from kuberider.settings.app_settings import app


class ContextsLoaderInteractor:
    def __init__(self):
        self.ct = CommandThread()

    def load_contexts(self):
        Kcb.init().command("config get-contexts --output='name'").start(
            self.ct,
            on_success=self.on_result,
            on_failure=self.on_result
        )

    def on_result(self, result):
        output = result['output']
        contexts = output.splitlines()
        app.data.save_contexts(contexts)
        app.data.signals.contexts_loaded.emit()


class CurrentContextInteractor:
    def __init__(self):
        self.ct = CommandThread()

    def current_context(self):
        Kcb.init().command("config current-contexts").start(
            self.ct,
            on_success=self.on_result,
            on_failure=self.on_result
        )

    def on_result(self, result):
        output = result['output']
        app.data.update_current_context(output)
        app.data.signals.context_changed.emit(output)


class ChangeContextInteractor:
    def update(self, new_context):
        app.data.update_current_context(new_context)
        app.data.signals.context_changed.emit(new_context)
