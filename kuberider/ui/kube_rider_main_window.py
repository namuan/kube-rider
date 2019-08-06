import logging
import sys
import traceback

from PyQt5.QtGui import QDesktopServices, QCloseEvent, QIcon
from PyQt5.QtWidgets import QMainWindow, QToolBar, qApp

from ..presenters.container_exec_presenter import ContainerExecPresenter
from ..presenters.pod_containers_presenter import PodContainersPresenter
from ..presenters.pod_events_presenter import PodEventsPresenter
from ..presenters.pod_list_presenter import PodListPresenter
from ..presenters.pod_logs_presenter import PodLogsPresenter
from ..presenters.pods_filter_presenter import PodsFilterPresenter
from ..presenters.watch_presenter import WatchPresenter
from ..generated.kube_rider_main import Ui_MainWindow
from ..presenters.console_presenter import ConsolePresenter
from ..presenters.file_menu_presenter import FileMenuPresenter
from ..presenters.kube_rider_main_presenter import KubeRiderMainPresenter
from ..presenters.toolbar_presenter import ToolbarPresenter
from ..ui.configuration_dialog import ConfigurationDialog
from ..ui.menus import menu_items
from ..ui.progress_dialog import ProgressDialog
from ..ui.shortcuts import shortcut_items
from ..ui.toolbar import toolbar_items
from ..ui.updater_dialog import Updater


class KubeRiderMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(KubeRiderMainWindow, self).__init__(parent)
        self.setupUi(self)

        # Add Components on Main Window
        self.updater = Updater(self)
        self.menu_bar = self.menuBar()
        self.toolbar = QToolBar()
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready', 5000)

        # Initialise Presenters
        self.presenter = KubeRiderMainPresenter(self)
        self.file_menu_presenter = FileMenuPresenter(self)
        self.toolbar_presenter = ToolbarPresenter(self.toolbar)
        self.pod_list_presenter = PodListPresenter(self.lst_pods)
        self.console_presenter = ConsolePresenter(self.console_text_edit)
        self.watch_presenter = WatchPresenter(self)
        self.pod_containers_presenter = PodContainersPresenter(self.lst_pod_containers)
        self.pod_events_presenter = PodEventsPresenter(self.txt_pod_events)
        self.pods_filter_presenter = PodsFilterPresenter(self)
        self.pod_logs_presenter = PodLogsPresenter(self)
        self.container_exec_presenter = ContainerExecPresenter(self)

        # Custom Dialogs
        self.progress_dialog = ProgressDialog(self)
        self.configuration_dialog = ConfigurationDialog(self)

        # Initialise Components
        menu_items(self)
        toolbar_items(self)
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
            toolbar_actions = self.toolbar.actions()
            updates_action = next(act for act in toolbar_actions if act.text() == 'Update Available')
            if updates_action:
                updates_action.setIcon(QIcon(":/images/download-48.png"))
                updates_action.setEnabled(True)

    def open_releases_page(self) -> None:
        QDesktopServices.openUrl(self.releases_page)
