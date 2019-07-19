from kuberider.settings.app_settings import app


class Kcb:
    command = ""

    @staticmethod
    def build(command):
        kubectl_path = app.load_kubectl_path()
        c = Kcb()
        c.command = f"{kubectl_path} {command}"
        return c

    def start(self, command_thread, on_success=None, on_failure=None):
        command_thread.command = self.command
        command_thread.signals.success.connect(on_success)
        command_thread.signals.failure.connect(on_failure)
        command_thread.start()
