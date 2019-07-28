from kuberider.domain.interactor import Interactor
from kuberider.settings.app_settings import app


class ContextsLoaderInteractor(Interactor):
    def __init__(self):
        super().__init__(
            on_success=self.on_result, on_failure=self.on_result
        )

    def load_contexts(self):
        self.kcb.command("config get-contexts --output='name'").start()

    def on_result(self, result):
        output = result['output']
        contexts = output.splitlines()
        app.data.save_contexts(contexts)
        app.data.signals.contexts_loaded.emit()


class CurrentContextInteractor(Interactor):
    def __init__(self):
        super().__init__(
            on_success=self.on_result, on_failure=self.on_result
        )

    def current_context(self):
        self.kcb.command("config current-context").start()

    def on_result(self, result):
        output = result['output']
        app.data.update_current_context(output)
        app.data.signals.context_changed.emit(output)


class ChangeContextInteractor(Interactor):
    def update_context(self, new_context):
        app.data.update_current_context(new_context)
