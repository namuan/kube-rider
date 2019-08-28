import logging

from kuberider.domain.contexts_interactor import ChangeContextInteractor, CurrentContextInteractor, \
    ContextsLoaderInteractor
from kuberider.domain.namespaces_interactor import NamespacesLoaderInteractor, ChangeNamespaceInteractor
from kuberider.settings.app_settings import app


class ToolbarPresenter:
    def __init__(self, toolbar):
        self.toolbar = toolbar
        self.contexts_loader = ContextsLoaderInteractor()
        self.namespaces = NamespacesLoaderInteractor()
        self.change_context = ChangeContextInteractor()
        self.current_context = CurrentContextInteractor()
        self.change_namespace = ChangeNamespaceInteractor()
        self.contexts_loaded = False
        self.namespaces_loaded = False

        # events
        app.data.signals.contexts_loaded.connect(self.on_contexts_loaded)
        app.data.signals.context_changed.connect(self.on_current_context_changed)
        app.data.signals.namespaces_loaded.connect(self.on_namespaces_loaded)

    def on_toolbar_load_contexts(self):
        self.contexts_loader.load_contexts()

    def __get_combox_box(self, action_name):
        toolbar_actions = self.toolbar.actions()
        tags_list_action = next(act for act in toolbar_actions if act.text() == action_name)
        return tags_list_action.defaultWidget()

    def on_namespaces_loaded(self):
        namespaces_ui = self.__get_combox_box("Namespaces")
        namespaces_ui.clear()
        namespaces = app.data.load_namespaces()
        for ns in namespaces:
            namespaces_ui.addItem(ns)

        self.namespaces_loaded = True
        if namespaces:
            self.on_current_namespace_changed(namespaces[0])

    def on_contexts_loaded(self):
        contexts_ui = self.__get_combox_box("Contexts")
        contexts_ui.clear()
        contexts = app.data.load_contexts()
        for ctx in contexts:
            contexts_ui.addItem(ctx)

        self.contexts_loaded = True
        self.current_context.current_context()

    def on_current_context_changed(self, new_context_name):
        if self.contexts_loaded:
            self.namespaces_loaded = False
            self.change_context.update_context(new_context_name)
            self.namespaces.load_namespaces()

    def on_current_namespace_changed(self, new_namespace_name):
        if self.namespaces_loaded:
            logging.info(f"Current namespace changed to {new_namespace_name}. Should get pods")
            self.change_namespace.update_namespace(new_namespace_name)
