import logging
from pathlib import Path
from tempfile import mktemp

from kuberider.domain.interactor import Interactor
from kuberider.settings.app_settings import app


class KubeResourceInteractor(Interactor):
    def __init__(self):
        super().__init__(on_success=self.on_result, on_failure=self.on_result)

    def write_temp_file(self, file_contents):
        tmp_file_name = mktemp(prefix="kuberider", suffix=".yaml")
        output = Path(tmp_file_name).write_text(file_contents)
        logging.info(f"Written {output} chars to {tmp_file_name}")
        return tmp_file_name

    def run(self, resource_definition):
        app.data.signals.command_started.emit("Applying Resource", True)
        temp_resource_file = self.write_temp_file(resource_definition)
        self.kcb.ctx().ns().command(f"apply -f {temp_resource_file}").start()

    def on_result(self, result):
        output = result['output']
        app.data.save_kube_resource(output)
