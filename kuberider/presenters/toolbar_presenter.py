from kuberider.settings.app_settings import app


class ToolbarPresenter:
    def __init__(self, toolbar):
        self.toolbar = toolbar

        # events
        app.data.signals.contexts_loaded.connect(self.on_contexts_loaded)
        app.data.signals.context_changed.connect(self.on_context_changed)

    def __get_combox_box(self, action_name):
        toolbar_actions = self.toolbar.actions()
        tags_list_action = next(act for act in toolbar_actions if act.text() == action_name)
        return tags_list_action.defaultWidget()

    def on_context_changed(self, context_name):
        contexts_ui = self.__get_combox_box("Contexts")
        contexts_ui.setCurrentText(context_name)

    def on_contexts_loaded(self):
        contexts_ui = self.__get_combox_box("Contexts")
        contexts_ui.clear()
        contexts = app.data.load_contexts()
        for ctx in contexts:
            contexts_ui.addItem(ctx)
