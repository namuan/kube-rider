from kuberider.domain.contexts_interactor import ChangeContextInteractor
from kuberider.domain.namespaces_interactor import NamespacesLoaderInteractor
from kuberider.settings.app_settings import app


class ToolbarPresenter:
    def __init__(self, toolbar):
        self.toolbar = toolbar
        self.namespaces = NamespacesLoaderInteractor()
        self.change_context = ChangeContextInteractor()
        self.contexts_loaded = False

        # events
        app.data.signals.contexts_loaded.connect(self.on_contexts_loaded)
        app.data.signals.context_changed.connect(self.on_context_changed)
        app.data.signals.namespaces_loaded.connect(self.on_namespaces_loaded)

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

    def on_context_changed(self, context_name):
        contexts_ui = self.__get_combox_box("Contexts")
        contexts_ui.setCurrentText(context_name)
        self.namespaces.load_namespaces()

    def on_contexts_loaded(self):
        contexts_ui = self.__get_combox_box("Contexts")
        contexts_ui.clear()
        contexts = app.data.load_contexts()
        for ctx in contexts:
            contexts_ui.addItem(ctx)

        self.contexts_loaded = True

    def on_current_context_changed(self, new_context_name):
        if self.contexts_loaded:
            self.change_context.update(new_context_name)
