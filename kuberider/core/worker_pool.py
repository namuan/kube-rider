import logging
import os

from PyQt5.QtCore import QThread, pyqtSignal, QObject

from kuberider.core.console_manager import ConsoleManager
from kuberider.core.mock_console_manager import MockConsoleManager
from kuberider.settings.app_settings import app

is_offline = os.getenv("MOCKED", "false").lower() == "true"


class CommandSignals(QObject):
    started = pyqtSignal(str)
    finished = pyqtSignal(str)
    success = pyqtSignal(dict)
    failure = pyqtSignal(dict)


class CommandThread(QThread):
    def __init__(self):
        self.signals = CommandSignals()
        self._command = None
        self.console_manager = MockConsoleManager() if is_offline else ConsoleManager()
        QThread.__init__(self)

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value

    def run(self):
        if not self._command:
            logging.warning("No Commands to run")
            return
        try:
            app.data.save_command(self._command)
            self.signals.started.emit(self._command)
            output = self.console_manager.run_command(self._command)
            result = {
                'command': self._command,
                'status': True,
                'output': output
            }
            self.signals.success.emit(result)
        except Exception as e:
            result = {
                'command': self._command,
                'status': False,
                'output': e
            }
            self.signals.failure.emit(result)
        finally:
            self.signals.finished.emit(self._command)
