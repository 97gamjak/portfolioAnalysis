from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QHBoxLayout,
    QLabel,
    QLineEdit,
)
from PyQt6.QtGui import QDoubleValidator

from views.validators import UpperCaseValidator
from enums.optionType import OptionType


class AddOptionView:
    def __init__(self):
        self.option_type_widget = QComboBox()

        for value in OptionType.values():
            self.option_type_widget.addItem(value)

        self.ticker_widget = QLineEdit()
        self.ticker_widget.setPlaceholderText("Ticker")
        self.ticker_widget.setValidator(UpperCaseValidator())

        self.premium_widget = QLineEdit()
        self.premium_widget.setPlaceholderText("Premium")
        self.premium_widget.setValidator(QDoubleValidator())

        self.strike_widget = QLineEdit()
        self.strike_widget.setPlaceholderText("Strike Price")
        self.strike_widget.setValidator(QDoubleValidator())

        self.underlying_price_widget = QLineEdit()
        self.underlying_price_widget.setPlaceholderText("Underlying Price")
        self.underlying_price_widget.setValidator(QDoubleValidator())

        self.expiration_widget = QDateEdit()
        self.expiration_widget.setCalendarPopup(True)
        self.expiration_widget.setDisplayFormat("dd-MM-yyyy")
        self.expiration_widget.setDate(QDate.currentDate())
        self.expiration_label = QLabel("Expiration Date:")
        self.expiration_label.setFixedHeight(10)
        self.expiration_label.setMaximumHeight(10)

        self.expiration_layout = QHBoxLayout()
        self.expiration_layout.addWidget(self.expiration_label)
        self.expiration_layout.addWidget(self.expiration_widget)

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
    def expiration(self):
        return self.expiration_widget.date()
