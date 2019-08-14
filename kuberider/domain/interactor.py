from kuberider.core.kube_command_builder import Kcb
from kuberider.core.worker_pool import CommandThread
from kuberider.settings.app_settings import app


class Interactor:
    def __init__(self, on_success=None, on_failure=None):
        self.ct = CommandThread()

        self.ct.signals.success.connect(on_success or self.default_on_success)
        self.ct.signals.failure.connect(on_failure or self.default_on_failure)

        self.kcb = Kcb.init(self.ct)

    def default_on_success(self, result):
        raise SyntaxError(f"Should at least implement on success handler: {result}")

    def default_on_failure(self, result):
        app.data.save_command_error(result['output'])
