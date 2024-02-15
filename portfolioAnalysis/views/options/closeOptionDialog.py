from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)


class CloseOptionDialog(QDialog):
    def __init__(self, controller, index):
        super().__init__()
        self.controller = controller
        self.index = index

        self.setWindowTitle("Close Option")

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

        layout.addLayout(vbox1)
        self.setLayout(layout)
