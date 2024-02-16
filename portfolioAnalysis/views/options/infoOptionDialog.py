from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from utils.stringUtils import double_to_percentage


class InfoOptionDialog(QDialog):
    def __init__(self, controller, index=None):
        super().__init__()
        self.controller = controller
        self.index = index

        self.setWindowTitle("Option Details")

        self.option = self.controller.get_option(index)
        self.underlying = self.controller.get_underlying_by_option(self.option)
        currency = self.option.currency

        layout = QVBoxLayout()

        header = QLabel(self.get_header())
        header.setStyleSheet("font-size: 18px; font-weight: bold;")

        layout.addWidget(header)

        initial_premium = QLabel("Initial Premium: ")
        initial_premium_value = QLabel(currency.transform(self.option.premium))

        vbox1 = QVBoxLayout()
        vbox1.addWidget(initial_premium)
        vbox1.addWidget(initial_premium_value)

        strike_price = QLabel("Strike Price: ")
        strike_price_value = QLabel(
            currency.transform(self.option.strike_price))

        vbox2 = QVBoxLayout()
        vbox2.addWidget(strike_price)
        vbox2.addWidget(strike_price_value)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        layout.addLayout(hbox)

        execution_date = QLabel("Execution Date: ")
        execution_date_value = QLabel(str(self.option.execution_date))

        vbox1 = QVBoxLayout()
        vbox1.addWidget(execution_date)
        vbox1.addWidget(execution_date_value)

        expiration_date = QLabel("Expiration Date: ")
        expiration_date_value = QLabel(str(self.option.expiration_date))

        vbox2 = QVBoxLayout()
        vbox2.addWidget(expiration_date)
        vbox2.addWidget(expiration_date_value)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        layout.addLayout(hbox)

        theoretical_yield = QLabel("Theoretical Yield: ")
        theoretical_yield_value = QLabel(
            double_to_percentage(self.option.theoretical_yield))

        vbox1 = QVBoxLayout()
        vbox1.addWidget(theoretical_yield)
        vbox1.addWidget(theoretical_yield_value)

        theoretical_yearly_yield = QLabel("Theoretical Yearly Yield: ")
        theoretical_yearly_yield_value = QLabel(
            double_to_percentage(self.option.theoretical_yearly_yield))

        vbox2 = QVBoxLayout()
        vbox2.addWidget(theoretical_yearly_yield)
        vbox2.addWidget(theoretical_yearly_yield_value)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        layout.addLayout(hbox)

        layout.addStretch()

        premium_evolution = QLabel("Premium Evolution")
        premium_evolution_table, sc = self.setup_premium_evolution_table()

        layout.addWidget(premium_evolution)
        layout.addWidget(premium_evolution_table)
        layout.addWidget(sc)
        self.setLayout(layout)

    def get_header(self):
        return str(self.option.option_type) + " " + self.underlying.company_name + "(" + self.underlying.ticker + ")"

    def setup_premium_evolution_table(self):
        self.option_premiums = self.controller.get_option_premiums_by_option(
            self.option)

        header = ["Date", "Premium"]

        table_widget = QTableWidget(len(self.option_premiums), len(header))
        table_widget.setHorizontalHeaderLabels(header)
        for i, premium in enumerate(self.option_premiums):
            table_widget.setItem(i, 0, QTableWidgetItem(str(premium.date)))
            table_widget.setItem(i, 1, QTableWidgetItem(
                self.option.currency.transform(premium.premium)))

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([premium.date for premium in self.option_premiums], [
            premium.premium for premium in self.option_premiums])

        return table_widget, sc


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
