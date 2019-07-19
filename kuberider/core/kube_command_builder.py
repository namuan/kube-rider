from kuberider.core.worker_pool import CommandThread
from kuberider.settings.app_settings import app


class Kcb:
    kubectl = None
    command = None
    ctx_param = None
    ns_param = None

    @staticmethod
    def init():
        c = Kcb()
        c.kubectl = app.load_kubectl_path()
        return c

    def command(self, command):
        self.command = command
        return self

    def ctx(self):
        self.ctx_param = f"--context {app.data.get_current_context()}"
        return self

    def ns(self):
        self.ns_param = f"--namespace {app.data.get_current_namespace()}"
        return self

    def complete_command(self):
        c = f"{self.kubectl}"
        if self.ctx_param:
            c += f" {self.ctx_param}"
        if self.ns_param:
            c += f" {self.ns_param}"
        if self.command:
            c += f" {self.command}"

        return c

    def start(self, command_thread: CommandThread, on_success=None, on_failure=None):
        command_thread.command = self.complete_command()
        command_thread.signals.success.connect(on_success)
        command_thread.signals.failure.connect(on_failure)
        command_thread.signals.started.connect(
            lambda c: app.data.update_command_status(c, started=True)
        )
        command_thread.signals.finished.connect(
            lambda c: app.data.update_command_status(c, started=False)
        )
        command_thread.start()
