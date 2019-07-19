import logging
from typing import List

from kuberider.entities.model import AppState
from kuberider.events.signals import AppSignals


class DataManager:
    signals = AppSignals()
    app_state = AppState()

    def save_contexts(self, contexts):
        logging.info(f"Contexts added: {len(contexts)}")
        self.app_state.contexts = contexts
        self.signals.contexts_loaded.emit()

    def load_contexts(self) -> List[str]:
        return self.app_state.contexts

    def save_command(self, new_command):
        logging.info(f"Command added: {new_command}")
        self.app_state.commands.append(new_command)
        self.signals.command_added.emit(new_command)

    def update_current_context(self, current_context):
        logging.info(f"Context changed: {current_context}")
        self.app_state.current_context = current_context
        self.signals.context_changed.emit(current_context)

    def update_command_status(self, command, started=False):
        if started:
            self.signals.command_started.emit(command)
        else:
            self.signals.command_finished.emit(command)
