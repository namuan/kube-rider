from kuberider.core.kube_command_builder import Kcb
from kuberider.core.worker_pool import CommandThread


class Interactor:
    def __init__(self, on_success=None, on_failure=None):
        self.ct = CommandThread()

        if on_success:
            self.ct.signals.success.connect(on_success)
        if on_failure:
            self.ct.signals.failure.connect(on_failure)

        self.kcb = Kcb.init(self.ct)
