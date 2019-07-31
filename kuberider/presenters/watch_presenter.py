import logging

from PyQt5.QtCore import QTimer

from kuberider.settings.app_settings import app


class WatchPresenter:
    def __init__(self, view):
        self.view = view
        self.timer = QTimer()

        # ui events
        self.view.chk_watch.stateChanged.connect(self.update_timer)
        self.timer.timeout.connect(self.on_timer_timeout)

    def update_timer(self):
        currently_watching = self.view.chk_watch.isChecked()
        watch_interval_secs = self.view.txt_watch_interval.value()
        if currently_watching:
            logging.info(f"Watching Pods every {watch_interval_secs} secs")
            self.timer.start(watch_interval_secs * 1000)
        else:
            self.timer.stop()
            logging.info(f"Stopped watching Pods")

    def on_timer_timeout(self):
        app.commands.reload_pods.emit()
