from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QDialogButtonBox,
    QMessageBox,
)

from views.options.addOptionView import AddOptionView
from views.options.ambiguousTickerDialog import AmbiguousTickerDialog


class AddOptionDialog(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("HELLO!")

        button_box = QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(button_box)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.add_option_view = AddOptionView()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.add_option_view.option_type_widget)
        self.layout.addWidget(self.add_option_view.ticker_widget)
        self.layout.addWidget(self.add_option_view.premium_widget)
        self.layout.addWidget(self.add_option_view.strike_widget)
        self.layout.addWidget(self.add_option_view.underlying_price_widget)
        self.layout.addLayout(self.add_option_view.expiration_layout)
        self.layout.addWidget(self.add_option_view.expiration_widget)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.want_to_close = False

        self.buttonBox.accepted.connect(self.add_option)

        self.controller.invalid_ticker.connect(self.invalid_ticker)
        self.controller.ambiguous_ticker.connect(self.ambiguous_ticker)
        self.controller.add_option_successful.connect(
            self.add_option_successful)

    def accept(self):
        if self.want_to_close:
            super().accept()

    def add_option(self):
        self.want_to_close = False
        self.ticker_is_valid = True
        self.controller.validate_ticker(self.add_option_view.ticker)

        if self.ticker_is_valid:
            self.controller.add_option(self.add_option_view)

    def add_option_successful(self, success, message):
        if success:
            self.want_to_close = True
            self.accept()
        else:
            self.want_to_close = False
            self.error_box = QMessageBox()
            self.error_box.warning(self, "Error", message)

    def invalid_ticker(self):
        self.error_box = QMessageBox()
        self.error_box.warning(self, "Error", "Ticker can not be found")
        self.ticker_is_valid = False

    def ambiguous_ticker(self, ambiguous_tickers):
        self.ambiguous_ticker_dialog = AmbiguousTickerDialog(ambiguous_tickers)
        self.ambiguous_ticker_dialog.exec()

        if self.ambiguous_ticker_dialog.ticker:
            self.add_option_view.ticker_widget.setText(
                self.ambiguous_ticker_dialog.ticker)
        else:
            self.add_option_view.ticker_widget.setText("")
            self.ticker_is_valid = False
