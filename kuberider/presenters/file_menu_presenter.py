import logging


class FileMenuPresenter:
    def __init__(self, parent):
        self.main_window = parent

    def on_file_new(self):
        logging.info("File New Menu triggered")
