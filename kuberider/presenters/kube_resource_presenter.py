from kuberider.domain.kube_resource_interactor import KubeResourceInteractor
from kuberider.settings.app_settings import app
from kuberider.ui.kube_resource_dialog import KubeResourceDialog


class KubeResourcePresenter:
    def __init__(self, parent):
        self.parent = parent
        self.dialog = KubeResourceDialog(self.parent)
        self.kube_apply = KubeResourceInteractor()

        # domain events
        app.data.signals.kube_resource_applied.connect(self.on_kube_resource_applied)

        # ui events
        self.dialog.btn_apply_resource.clicked.connect(self.apply_resource)
        self.dialog.btn_close_dialog.clicked.connect(self.hide_dialog)

    def show_dialog(self):
        self.dialog.txt_resource_definition.clear()
        self.dialog.lbl_command_output.clear()
        self.dialog.show()

    def apply_resource(self):
        resource_definition = self.dialog.txt_resource_definition.toPlainText()
        self.kube_apply.run(resource_definition)

    def on_kube_resource_applied(self, output):
        self.dialog.lbl_command_output.setText(output)

    def hide_dialog(self):
        self.dialog.hide()
