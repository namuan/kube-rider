from PyQt5.QtWidgets import QInputDialog, QLineEdit

from kuberider.domain.container_interactor import ExecShellInteractor
from kuberider.settings.app_settings import app


class ContainerExecPresenter:
    def __init__(self, parent):
        self.parent = parent
        self.exec_shell = ExecShellInteractor()

        # commands
        app.commands.on_exec_shell.connect(self.on_exec_shell)

    def on_exec_shell(self, pod_name, container_name):
        cmd, ret = QInputDialog.getText(self.parent, "Enter command to run in the container", "Command", QLineEdit.Normal)
        if ret and cmd:
            self.exec_shell.run(pod_name, container_name, cmd)
