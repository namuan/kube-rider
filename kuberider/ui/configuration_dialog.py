from PyQt5.QtWidgets import (QDialog)

from ..presenters.configuration_presenter import ConfigurationPresenter
from ..generated.configuration_dialog import Ui_Configuration


class ConfigurationDialog(QDialog, Ui_Configuration):

    def __init__(self, parent=None):
        super(ConfigurationDialog, self).__init__(parent)
        self.presenter = ConfigurationPresenter(self, parent)

    def initialize(self):
        self.setupUi(self)

    def show_dialog(self):
        self.presenter.load_configuration_dialog()
