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
    partial_output = pyqtSignal(str)


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
            app.data.save_command(self.command)
            self.signals.started.emit(self.command)
            output = self.console_manager.run_command(self.command)
            result = {
                'command': self.command,
                'status': True,
                'output': output
            }
            self.signals.success.emit(result)
        except Exception as e:
            logging.error(e)
            result = {
                'command': self.command,
                'status': False,
                'output': e
            }
            self.signals.failure.emit(result)
        finally:
            self.signals.finished.emit(self.command)


class TailCommandThread(QThread):
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
        logging.info(f"Running Tail Command Thread")
        self.console_manager.abort_long_running_command = False
        app.data.save_command(self.command)
        self.signals.started.emit(self.command)
        for line in self.console_manager.run_long_running_command(self.command):
            self.signals.partial_output.emit(line.strip().decode('utf-8'))

    def stop_process(self):
        self.console_manager.abort_long_running_command = True
