import logging


class EmptyFramePresenter:
    def __init__(self, view):
        self.view = view

    def test_shortcut(self):
        logging.info("Shortcut triggered")

    def display(self):
        self.view.show()
