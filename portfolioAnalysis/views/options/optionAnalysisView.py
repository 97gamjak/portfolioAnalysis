from PyQt6.QtWidgets import (
    QDialog,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHeaderView,
)

from portfolioAnalysis.utils.stringUtils import double_to_percentage


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

        header = [
            "Option\nType",
            "Underlying\nTicker",
            "Total\nDays",
            "Days\nLeft",
            "Past\nTime",
            "Avg.\nStrike",
            "Total\nPremium",
            "Yield",
            "Yearly\nYield",
        ]

        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)
        self.setRowCount(len(self.open_options))
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

        for i, option in enumerate(self.open_options):
            currency = option.currency

            self.setItem(i, 0, QTableWidgetItem(str(option.option_type)))
            self.setItem(i, 1, QTableWidgetItem(option.underlying_ticker))
            self.setItem(i, 2, QTableWidgetItem(str(option.total_days)))
            self.setItem(i, 3, QTableWidgetItem(
                str(option.days_to_expiration)))
            self.setItem(i, 4, QTableWidgetItem(
                double_to_percentage(option.past_time)))
            self.setItem(i, 5, QTableWidgetItem(
                currency.transform(option.avg_strike)))
            self.setItem(i, 6, QTableWidgetItem(
                currency.transform(option.total_premium)))
            self.setItem(i, 7, QTableWidgetItem(
                double_to_percentage(option.theoretical_yield)))
            self.setItem(i, 8, QTableWidgetItem(
                double_to_percentage(option.theoretical_yearly_yield)))


class ClosedOptionTableView(QTableWidget):
    def __init__(self, controller, repository):
        self.controller = controller
        self.repository = repository

        super().__init__()

    def update(self):

        self.closed_options = self.controller.get_closed_options()

        header = [
            "Option\nType",
            "Underlying\nTicker",
            "Total\nDays",
            "Actual\nDays",
            "Avg.\nStrike",
            "Total\nPremium",
            "Yield",
            "Yearly\nYield",
            "effective\nYield",
            "effective\nYearly\nYield",
        ]

        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)
        self.setRowCount(len(self.closed_options))
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

        for i, option in enumerate(self.closed_options):
            currency = option.currency

            self.setItem(i, 0, QTableWidgetItem(str(option.option_type)))
            self.setItem(i, 1, QTableWidgetItem(option.underlying_ticker))
            self.setItem(i, 2, QTableWidgetItem(str(option.total_days)))
            self.setItem(i, 3, QTableWidgetItem(
                str(option.actual_days)))
            self.setItem(i, 5, QTableWidgetItem(
                currency.transform(option.avg_strike)))
            self.setItem(i, 6, QTableWidgetItem(
                currency.transform(option.total_premium)))
            self.setItem(i, 7, QTableWidgetItem(
                currency.transform(option.total_commission)))
            self.setItem(i, 7, QTableWidgetItem(
                double_to_percentage(option.theoretical_yield)))
            self.setItem(i, 8, QTableWidgetItem(
                double_to_percentage(option.theoretical_yearly_yield)))
            self.setItem(i, 9, QTableWidgetItem(
                double_to_percentage(option.effective_yield)))
            self.setItem(i, 10, QTableWidgetItem(
                double_to_percentage(option.effective_yearly_yield)))
