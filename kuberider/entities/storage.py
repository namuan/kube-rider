from PyQt5.QtCore import QRunnable, pyqtSlot


class StorageTask(QRunnable):

    def _save_entity(self):
        pass

    @pyqtSlot()
    def run(self):
        self._save_entity()
