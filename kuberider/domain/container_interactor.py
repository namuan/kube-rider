import logging

from kuberider.domain.interactor import Interactor


class ExecShellInteractor(Interactor):
    def __init__(self):
        super().__init__(on_success=None, on_failure=None)

    def run(self, pod_name, container_name, shell_cmd):
        cmd = self.kcb.ctx().ns().command(
            f"exec {pod_name} -c {container_name} {shell_cmd}"
        ).complete_command()
        # Convert cmd to OS specific command to run in an external app
        # Then set the command on self.kcb
        # And start
        self.kcb.command("hello World")
        self.kcb.start()
        logging.info(f"External App: {cmd}")
