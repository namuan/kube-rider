from kuberider.core.worker_pool import CommandThread
from kuberider.settings.app_settings import app


class Kcb:
    command = ""

    @staticmethod
    def build(command):
        kubectl_path = app.load_kubectl_path()
        c = Kcb()
        c.command = f"{kubectl_path} {command}"
        return c

    def start(self, command_thread: CommandThread, on_success=None, on_failure=None):
        command_thread.command = self.command
        command_thread.signals.success.connect(on_success)
        command_thread.signals.failure.connect(on_failure)
        command_thread.signals.started.connect(
            lambda c: app.data.update_command_status(c, started=True)
        )
        command_thread.signals.finished.connect(
            lambda c: app.data.update_command_status(c, started=False)
        )
        command_thread.start()
