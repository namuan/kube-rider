class Kcb:
    command = ""

    @staticmethod
    def build(command):
        c = Kcb()
        c.command = f"kubectl {command}"
        return c

    def start(self, command_thread, on_success=None, on_failure=None):
        command_thread.command = self.command
        command_thread.signals.success.connect(on_success)
        command_thread.signals.failure.connect(on_failure)
        command_thread.start()
