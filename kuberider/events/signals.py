from PyQt5.QtCore import QObject, pyqtSignal


class AppSignals(QObject):
    contexts_loaded = pyqtSignal()
    command_added = pyqtSignal(str)
    context_changed = pyqtSignal(str)
    command_started = pyqtSignal(str)
    command_finished = pyqtSignal(str)
    namespaces_loaded = pyqtSignal()
    namespace_changed = pyqtSignal(str)
    pods_loaded = pyqtSignal(list)

