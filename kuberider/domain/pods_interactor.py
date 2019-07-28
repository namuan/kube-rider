from kuberider.domain.interactor import Interactor
from kuberider.entities.model import KubePods
from kuberider.settings.app_settings import app


class GetPodsInteractor(Interactor):
    def __init__(self):
        super().__init__(on_success=self.on_result, on_failure=self.on_result)

    def run(self):
        self.kcb.ctx().ns().command("get pods -o json").start()

    def on_result(self, result):
        output = result['output']
        kube_pods: KubePods = KubePods.from_json_str(output)
        pods = [pod for pod in kube_pods.items]
        app.data.save_pods(pods)

