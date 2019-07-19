from PyQt5.QtWidgets import (QDialog)

from ..generated.configuration_dialog import Ui_Configuration
from ..presenters.configuration_presenter import ConfigurationPresenter


class ConfigurationDialog(QDialog, Ui_Configuration):

    def __init__(self, parent=None):
        super(ConfigurationDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.presenter = ConfigurationPresenter(self, parent)

    def show_dialog(self):
        self.presenter.load_configuration_dialog()
