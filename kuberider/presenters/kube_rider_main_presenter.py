import logging

from kuberider.domain.contexts_interactor import ContextsLoaderInteractor
from kuberider.settings.app_settings import app


class KubeRiderMainPresenter:
    def __init__(self, view):
        self.view = view
        self.initial_load = True
        app.init()
        app.init_logger()
        if app.geometry():
            self.view.restoreGeometry(app.geometry())
        if app.window_state():
            self.view.restoreState(app.window_state())



    def after_window_loaded(self):
        if not self.initial_load:
            return

        self.initial_load = False
        self.check_updates()

    def check_updates(self):
        if app.load_updates_configuration():
            self.view.updater.check()

    def save_settings(self):
        logging.info("Saving settings for Main Window")
        app.save_window_state(
            geometry=self.view.saveGeometry(),
            window_state=self.view.saveState()
        )

    def shutdown(self):
        self.save_settings()
