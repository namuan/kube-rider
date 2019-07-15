import logging

from kuberider.kube_contexts.contexts_interactor import KubeContextsLoader
from kuberider.settings.app_settings import app_settings


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

        self.kube_contexts_loader = KubeContextsLoader()

    def after_window_loaded(self):
        if not self.initial_load:
            return

        self.initial_load = False
        self.refresh_app()
        self.check_updates()

    def refresh_app(self):
        self.kube_contexts_loader.load_contexts()

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
        self.save_settings()
