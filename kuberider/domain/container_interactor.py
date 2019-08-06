from kuberider.core.kube_command_builder import Kcb
from kuberider.core.worker_pool import ExternalAppCommandThread
from kuberider.settings.app_settings import app


class ExecShellInteractor:
    def __init__(self):
        self.ct = ExternalAppCommandThread()
        self.kcb = Kcb.init(self.ct)

    def run(self, pod_name, container_name, shell_cmd):
        cmd = self.kcb.ctx().ns().command(
            f"exec {pod_name} -c {container_name} {shell_cmd}"
        ).complete_command()
        app.data.save_command(cmd)
        self.kcb.start_command(cmd)
