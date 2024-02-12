from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
)
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from typing import Optional

from views.validators import UpperCaseValidator
from enums.optionType import OptionType
from models.option import Option


class AddOptionView:
    def __init__(self, option: Optional[Option] = None):
        self.option_type_widget = QComboBox()

        self.setup_layout()

        if option is not None:
            print("Option is not None")
            self.option_type_widget.setCurrentText(option.option_type.value)
            self.ticker_widget.setText(option.underlying_ticker)
            self.premium_widget.setText(str(option.premium))
            self.strike_widget.setText(str(option.strike_price))
            self.shares_widget.setText(str(option.shares))
            self.underlying_shares_widget.setText(
                str(option.underlying_shares))
            self.underlying_price_widget.setText(
                str(option.underlying_price) if option.underlying_price is not None else "")
            self.expiration_widget.setDate(option.expiration_date)
            self.execution_widget.setDate(option.execution_date)

    def setup_layout(self):
        for value in OptionType.values():
            self.option_type_widget.addItem(value)

        self.labels = []

        self.ticker_label = QLabel("Underlying Ticker/Asset Name:")
        self.labels.append(self.ticker_label)
        self.ticker_widget = self.init_line_edit(
            "Underlying Ticker/Asset Name", UpperCaseValidator())

        self.premium_label = QLabel("Premium Price:")
        self.labels.append(self.premium_label)
        self.premium_widget = self.init_line_edit(
            "Premium Price", QDoubleValidator())

        self.strike_label = QLabel("Strike Price:")
        self.labels.append(self.strike_label)
        self.strike_widget = self.init_line_edit(
            "Strike Price", QDoubleValidator())

        self.shares_label = QLabel("Number of Shares:")
        self.labels.append(self.shares_label)
        self.shares_widget = self.init_line_edit(
            "Number of Shares", QIntValidator(), "1")

        self.underlying_shares_label = QLabel("Number of Underlying Shares:")
        self.labels.append(self.underlying_shares_label)
        self.underlying_shares_widget = self.init_line_edit(
            "Number of Underlying Shares", QIntValidator(), "100")

        self.underlying_price_label = QLabel("Underlying Price:")
        self.labels.append(self.underlying_price_label)
        self.underlying_price_widget = self.init_line_edit(
            "Underlying Price", QDoubleValidator())

        self.execution_widget = self.init_qdate_edit()
        self.execution_label = QLabel("Execution Date:")
        self.labels.append(self.execution_label)
        self.execution_layout = QHBoxLayout()
        self.execution_layout.addWidget(self.execution_label)
        self.execution_layout.addWidget(self.execution_widget)

        self.expiration_widget = self.init_qdate_edit()
        self.expiration_label = QLabel("Expiration Date:")
        self.labels.append(self.expiration_label)
        self.expiration_layout = QHBoxLayout()
        self.expiration_layout.addWidget(self.expiration_label)
        self.expiration_layout.addWidget(self.expiration_widget)

        for label in self.labels:
            label.setFixedHeight(10)
            label.setMaximumHeight(10)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.option_type_widget)
        self.layout.addWidget(self.ticker_label)
        self.layout.addWidget(self.ticker_widget)
        self.layout.addWidget(self.premium_label)
        self.layout.addWidget(self.premium_widget)
        self.layout.addWidget(self.strike_label)
        self.layout.addWidget(self.strike_widget)
        self.layout.addWidget(self.shares_label)
        self.layout.addWidget(self.shares_widget)
        self.layout.addWidget(self.underlying_shares_label)
        self.layout.addWidget(self.underlying_shares_widget)
        self.layout.addWidget(self.underlying_price_label)
        self.layout.addWidget(self.underlying_price_widget)
        self.layout.addLayout(self.execution_layout)
        self.layout.addLayout(self.expiration_layout)

    def init_line_edit(self, place_holder: str, validator, default_value: str = ""):
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(place_holder)
        line_edit.setValidator(validator)
        line_edit.setText(default_value)
        return line_edit

    def init_qdate_edit(self):
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDisplayFormat("dd-MM-yyyy")
        date_edit.setDate(QDate.currentDate())
        return date_edit

    @property
    def option_type(self):
        return self.option_type_widget.currentText()

    @property
    def ticker(self):
        return self.ticker_widget.text()

    @property
    def premium(self):
        return self.premium_widget.text()

    @property
    def strike(self):
        return self.strike_widget.text()

    @property
    def underlying_price(self):
        return self.underlying_price_widget.text()

    @property
    def execution_date(self):
        return self.execution_widget.date()

    @property
    def expiration_date(self):
        return self.expiration_widget.date()

    @property
    def shares(self):
        return self.shares_widget.text()

    @property
    def underlying_shares(self):
        return self.underlying_shares_widget.text()
