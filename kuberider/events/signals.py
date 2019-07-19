from PyQt5.QtCore import QObject, pyqtSignal


class AppSignals(QObject):
    contexts_loaded = pyqtSignal()
    command_added = pyqtSignal(str)
    context_changed = pyqtSignal(str)
    command_started = pyqtSignal(str)
    command_finished = pyqtSignal(str)
