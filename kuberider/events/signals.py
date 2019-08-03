from PyQt5.QtCore import QObject, pyqtSignal

from kuberider.entities.model import KubePodItem


class AppSignals(QObject):
    contexts_loaded = pyqtSignal()
    command_added = pyqtSignal(str)
    context_changed = pyqtSignal(str)
    command_started = pyqtSignal(str, bool)
    command_finished = pyqtSignal()
    namespaces_loaded = pyqtSignal()
    namespace_changed = pyqtSignal()
    pods_loaded = pyqtSignal(list)
    pod_selected = pyqtSignal(KubePodItem)
    filter_enabled = pyqtSignal()
    filter_cleared = pyqtSignal()


class AppCommands(QObject):
    reload_pods = pyqtSignal()
    update_pods = pyqtSignal()
    log_pods = pyqtSignal()
    open_pod_logs = pyqtSignal(str, str)
