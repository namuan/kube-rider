class Kcb:
    kubectl = "kubectl"
    command = ""

    @classmethod
    def build(cls, command):
        c = cls()
        c.command = f"{cls.kubectl} {command}"
        return c

    def start(self, command_thread, on_success=None, on_failure=None):
        command_thread.command = self.command
        command_thread.signals.success.connect(on_success)
        command_thread.signals.failure.connect(on_failure)
        command_thread.start()
