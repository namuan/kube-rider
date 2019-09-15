from PyQt5.QtWidgets import QInputDialog, QLineEdit

from kuberider.domain.container_interactor import ExecShellInteractor
from kuberider.settings.app_settings import app


class ContainerExecPresenter:
    def __init__(self, parent):
        self.parent = parent
        self.exec_shell = ExecShellInteractor()

        # commands
        app.commands.on_exec_shell.connect(self.on_exec_shell)
        app.commands.on_port_forward.connect(self.on_port_forward)
        app.commands.on_follow_logs.connect(self.on_follow_logs)

    def on_exec_shell(self, pod_name, container_name):
        cmd, ret = QInputDialog.getText(self.parent, "Execute command", "Command",
                                        QLineEdit.Normal)
        if ret and cmd:
            self.exec_shell.run(pod_name, container_name, cmd)

    def on_port_forward(self, pod_name, container_name):
        cmd, ret = QInputDialog.getText(self.parent, "Port forwarding", "Enter Ports (Local:Remote)", QLineEdit.Normal)
        if ret and cmd:
            self.exec_shell.port_forward(pod_name, container_name, cmd)

    def on_follow_logs(self, pod_name, container_name):
        self.exec_shell.follow_logs(pod_name, container_name)
