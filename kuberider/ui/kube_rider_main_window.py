import logging
import sys
import traceback

from PyQt5.QtGui import QDesktopServices, QCloseEvent, QIcon
from PyQt5.QtWidgets import QMainWindow, QToolBar, qApp

from ..generated.kube_rider_main import Ui_MainWindow
from ..presenters.empty_frame_presenter import EmptyFramePresenter
from ..presenters.file_menu_presenter import FileMenuPresenter
from ..presenters.kube_rider_main_presenter import KubeRiderMainPresenter
from ..ui.configuration_dialog import ConfigurationDialog
from ..ui.empty_frame_window import EmptyFrameWindow
from ..ui.menus import menu_items
from ..ui.progress_dialog import ProgressDialog
from ..ui.shortcuts import shortcut_items
from ..ui.toolbar import tool_bar_items
from ..ui.updater_dialog import Updater


class KubeRiderMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(KubeRiderMainWindow, self).__init__(parent)
        self.setupUi(self)

        # Empty Frame setup
        self.empty_frame_window = EmptyFrameWindow(self)
        self.empty_frame_presenter = EmptyFramePresenter(self.empty_frame_window)
        self.empty_frame_presenter.display()

        # Add Components on Main Window
        self.updater = Updater(self)
        self.menu_bar = self.menuBar()
        self.tool_bar = QToolBar()
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready', 5000)

        # Initialise Presenters
        self.presenter = KubeRiderMainPresenter(self)
        self.file_menu_presenter = FileMenuPresenter(self)

        # Custom Dialogs
        self.progress_dialog = ProgressDialog(self)
        self.configuration_dialog = ConfigurationDialog(self)

        # Initialise Components
        menu_items(self)
        tool_bar_items(self)
        shortcut_items(self)

        # Initialise Sub-Systems
        sys.excepthook = KubeRiderMainWindow.log_uncaught_exceptions

    @staticmethod
    def log_uncaught_exceptions(cls, exc, tb) -> None:
        logging.critical(''.join(traceback.format_tb(tb)))
        logging.critical('{0}: {1}'.format(cls, exc))

    # Main Window events
    def resizeEvent(self, event):
        self.presenter.after_window_loaded()

    def closeEvent(self, event: QCloseEvent):
        logging.info("Received close event")
        event.accept()
        self.presenter.shutdown()
        try:
            qApp.exit(0)
        except:
            pass

    # End Main Window events
    def check_updates(self):
        self.updater.check()

    def update_available(self, latest, current):
        update_available = True if latest > current else False
        logging.info(f"Update Available ({latest} > {current}) ? ({update_available}) Enable Toolbar Icon")
        if update_available:
            toolbar_actions = self.tool_bar.actions()
            updates_action = next(act for act in toolbar_actions if act.text() == 'Update Available')
            if updates_action:
                updates_action.setIcon(QIcon(":/images/download-48.png"))
                updates_action.setEnabled(True)

    def open_releases_page(self) -> None:
        QDesktopServices.openUrl(self.releases_page)
