from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QDialogButtonBox,
    QMessageBox,
)

from portfolioAnalysis.views.options.addOptionView import AddOptionView
from portfolioAnalysis.views.options.ambiguousTickerDialog import AmbiguousTickerDialog


class AddOptionDialog(QDialog):
    def __init__(self, controller, index=None):
        super().__init__()
        self.controller = controller
        self.index = index

        if index is None:
            self.setWindowTitle("Add Option")
            self.edit_mode = False
        else:
            self.setWindowTitle("Edit Option")
            self.edit_mode = True

        button_box = QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(button_box)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        if self.edit_mode:
            self.add_option_view = AddOptionView(
                self.controller.get_option(index))
        else:
            self.add_option_view = AddOptionView()

        self.layout = self.add_option_view.layout
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

        if self.ticker_is_valid and not self.edit_mode:
            self.controller.add_option(self.add_option_view)
        elif self.ticker_is_valid and self.edit_mode:
            self.controller.edit_option(self.add_option_view, self.index)

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
