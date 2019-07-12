import logging

from ..core.app_settings import app_settings
from ..core.worker_pool import single_worker


class KubeRiderMainPresenter:
    def __init__(self, view):
        self.view = view
        self.initial_load = True
        app_settings.init()
        app_settings.init_logger()
        if app_settings.geometry():
            self.view.restoreGeometry(app_settings.geometry())
        if app_settings.window_state():
            self.view.restoreState(app_settings.window_state())

    def after_window_loaded(self):
        if not self.initial_load:
            return

        self.initial_load = False
        self.refresh_app()
        self.check_updates()

    def refresh_app(self):
        self.show_frame()

    def show_frame(self):
        """Decide whether to display an empty frame or not"""
        app_ready = True
        if app_ready:
            logging.info(f"App Ready. Hiding Empty Frame")
            logging.info(f"App Ready. Showing Data Frame")
        else:
            logging.info(f"App Not Ready. Showing Empty Frame")
            logging.info(f"App Not Ready. Hiding Data Frame")

    def check_updates(self):
        if app_settings.load_updates_configuration():
            self.view.updater.check()

    def save_settings(self):
        logging.info("Saving settings for Main Window")
        app_settings.save_window_state(
            geometry=self.view.saveGeometry(),
            window_state=self.view.saveState()
        )

    def shutdown(self):
        single_worker.shutdown()
        self.save_settings()
