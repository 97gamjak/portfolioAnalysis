from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
)


class InfoOptionDialog(QDialog):
    def __init__(self, controller, index=None):
        super().__init__()
        self.controller = controller
        self.index = index

        self.setWindowTitle("Option Details")

        self.option = self.controller.get_option(index)
        self.underlying = self.controller.get_underlying_by_option(self.option)

        layout = QVBoxLayout()

        header = QLabel(self.get_header())
        header.setStyleSheet("font-size: 18px; font-weight: bold;")

        layout.addWidget(header)

        initial_premium = QLabel("Initial Premium: ")
        initial_premium_value = QLabel(self.option.premium_currency_string)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(initial_premium)
        vbox1.addWidget(initial_premium_value)

        strike_price = QLabel("Strike Price: ")
        strike_price_value = QLabel(self.option.strike_price_currency_string)

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

        layout.addStretch()

        premium_evolution = QLabel("Premium Evolution")
        premium_evolution_table = self.setup_premium_evolution_table()

        layout.addWidget(premium_evolution)
        layout.addWidget(premium_evolution_table)
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
            table_widget.setItem(i, 1, QTableWidgetItem(str(premium.premium)))

        return table_widget
