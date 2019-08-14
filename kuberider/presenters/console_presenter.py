from kuberider.settings.app_settings import app


class ConsolePresenter:
    def __init__(self, console_text_edit):
        self.console_text_edit = console_text_edit

        # domain events
        app.data.signals.command_added.connect(self.on_command_added)
        app.data.signals.command_failed.connect(self.on_command_failed)

    def on_command_added(self, new_command):
        self.console_text_edit.appendPlainText(new_command.replace(" -o json", ""))

    def on_command_failed(self, failure_message):
        message = f"[ERROR] {failure_message}"
        self.console_text_edit.appendPlainText(message)
