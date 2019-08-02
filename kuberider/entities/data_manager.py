import logging
from typing import List

import dataset

from kuberider.entities.model import AppState
from kuberider.events.signals import AppSignals


class DataManager:
    signals = AppSignals()
    app_state = AppState()

    def __init__(self, app_dir):
        db_path = f"sqlite:///{app_dir}/kuberider.db"
        self.db = dataset.connect(db_path)

    def save_command(self, new_command):
        logging.info(f"Command added: {new_command}")
        self.app_state.commands.append(new_command)
        self.signals.command_added.emit(new_command)

    def update_command_status(self, command, started=False):
        if started:
            self.signals.command_started.emit(command, True)
        else:
            self.signals.command_finished.emit()

    def update_app_state_in_db(self, app_state_entity: AppState):
        table = self.db[app_state_entity.record_type]
        table.upsert(
            dict(
                name=app_state_entity.record_type,
                object=app_state_entity.to_json_str()
            ),
            ['name']
        )

    def save_filter(self, filter):
        logging.info(f"Saving filter {filter} in AppState")
        self.app_state.pods_filter = filter
        self.update_app_state_in_db(self.app_state)

    def save_contexts(self, contexts):
        logging.info(f"Contexts added: {len(contexts)}")
        self.app_state.contexts = contexts
        self.update_app_state_in_db(self.app_state)

    def load_contexts(self) -> List[str]:
        return self.app_state.contexts

    def update_current_context(self, current_context):
        logging.info(f"Context changed: {current_context}")
        self.app_state.current_context = current_context
        self.update_app_state_in_db(self.app_state)

    def get_current_context(self) -> str:
        return self.app_state.current_context

    def save_namespaces(self, namespaces):
        logging.info(f"Namespaces added: {len(namespaces)}")
        self.app_state.namespaces = namespaces
        self.update_app_state_in_db(self.app_state)

    def update_current_namespace(self, current_namespace):
        logging.info(f"Namespace changed: {current_namespace}")
        self.app_state.current_namespace = current_namespace
        self.update_app_state_in_db(self.app_state)

    def load_namespaces(self):
        return self.app_state.namespaces

    def get_current_namespace(self):
        return self.app_state.current_namespace

    def save_pods(self, pods):
        self.signals.pods_loaded.emit(pods)
