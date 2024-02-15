from PyQt6.QtWidgets import (
    QDialog,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)


class OptionAnalysisView(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.repository = parent.repository.option_repository
        self.controller = parent.controller.option_controller

        self.options = QWidget()
        self.options.setObjectName(u"option analysis")

        self.open_option_table = self.setup_table_view(
            self.controller, self.repository, "open")
        self.closed_option_table = self.setup_table_view(
            self.controller, self.repository, "closed")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.open_option_table)
        self.closed_option_table = self.setup_table_view(
            self.controller, self.repository, "closed")
        self.layout.addWidget(self.closed_option_table)

        self.setLayout(self.layout)

    def setup_table_view(self, controller, repository, option_type):
        if option_type == "open":
            table_view = OpenOptionTableView(controller, repository)
        else:
            table_view = ClosedOptionTableView(controller, repository)

        return table_view

    def show(self):
        super().show()
        self.open_option_table.update()
        self.closed_option_table.update()


class OpenOptionTableView(QTableWidget):
    def __init__(self, controller, repository):
        self.controller = controller
        self.repository = repository

        super().__init__()

    def update(self):

        self.open_options = self.controller.get_open_options()

        header = ["Option Type", "Underlying Ticker"]

        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)
        self.setRowCount(len(self.open_options))

        for i, option in enumerate(self.open_options):
            self.setItem(i, 0, QTableWidgetItem(str(option.option_type)))
            self.setItem(i, 1, QTableWidgetItem(option.underlying_ticker))


class ClosedOptionTableView(QTableWidget):
    def __init__(self, controller, repository):
        self.controller = controller
        self.repository = repository

        super().__init__()

    def update(self):

        self.closed_options = self.controller.get_closed_options()

        header = ["Option Type", "Underlying Ticker"]

        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)
        self.setRowCount(len(self.closed_options))

        for i, option in enumerate(self.closed_options):
            self.setItem(i, 0, QTableWidgetItem(str(option.option_type)))
            self.setItem(i, 1, QTableWidgetItem(option.underlying_ticker))
