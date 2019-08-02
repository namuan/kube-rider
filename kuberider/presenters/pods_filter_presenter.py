from kuberider.domain.pods_interactor import FilterPodsInteractor


class PodsFilterPresenter:
    def __init__(self, view):
        self.view = view
        self.filter_pods = FilterPodsInteractor()

        # ui events
        self.view.btn_enable_filter.clicked.connect(self.enable_filter)
        self.view.btn_clear_filter.clicked.connect(self.clear_filter)

    def enable_filter(self):
        filter = self.view.txt_filter.text()
        self.filter_pods.apply_filter(filter)

    def clear_filter(self):
        self.view.txt_filter.setText("")
        self.filter_pods.clear_filter()
