from PyQt5.QtCore import QObject

from kuberider.core.worker_pool import CommandThread
from kuberider.settings.app_settings import app


class Kcb(QObject):
    kubectl = None
    command_thread = None
    _command = None
    ctx_param = None
    ns_param = None

    @staticmethod
    def init(command_thread: CommandThread):
        c = Kcb()
        c.kubectl = app.load_kubectl_path()
        c.command_thread = command_thread

        c.command_thread.signals.started.connect(
            lambda c: app.data.update_command_status(c, started=True)
        )
        c.command_thread.signals.finished.connect(
            lambda c: app.data.update_command_status(c, started=False)
        )

        return c

    def command(self, command):
        self._command = command
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
        if self._command:
            c += f" {self._command}"

        return c

    def start(self):
        self.command_thread.command = self.complete_command()
        self.command_thread.start()

    def start_command(self, command):
        self.command_thread.command = command
        self.command_thread.start()
