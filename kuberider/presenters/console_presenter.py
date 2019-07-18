from kuberider.settings.app_settings import app


class ConsolePresenter:
    def __init__(self, console_text_edit):
        self.console_text_edit = console_text_edit
        app.data.signals.command_added.connect(self.on_command_added)

    def on_command_added(self, new_command):
        self.console_text_edit.appendPlainText(new_command)
