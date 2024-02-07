from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QHBoxLayout,
    QLabel,
    QLineEdit,
)
from PyQt6.QtGui import QDoubleValidator
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
            self.underlying_price_widget.setText(
                str(option.underlying_price) if option.underlying_price is not None else "")
            self.expiration_widget.setDate(option.expiration_date)
            self.execution_widget.setDate(option.execution_date)

    def setup_layout(self):
        for value in OptionType.values():
            self.option_type_widget.addItem(value)

        self.ticker_label = QLabel("Underlying Ticker/Name:")
        self.ticker_label.setFixedHeight(10)
        self.ticker_label.setMaximumHeight(10)
        self.ticker_widget = QLineEdit()
        self.ticker_widget.setPlaceholderText("Underlying Ticker/Name")
        self.ticker_widget.setValidator(UpperCaseValidator())

        self.premium_label = QLabel("Premium Price:")
        self.premium_label.setFixedHeight(10)
        self.premium_label.setMaximumHeight(10)
        self.premium_widget = QLineEdit()
        self.premium_widget.setPlaceholderText("Premium Price")
        self.premium_widget.setValidator(QDoubleValidator())

        self.strike_label = QLabel("Strike Price:")
        self.strike_label.setFixedHeight(10)
        self.strike_label.setMaximumHeight(10)
        self.strike_widget = QLineEdit()
        self.strike_widget.setPlaceholderText("Strike Price")
        self.strike_widget.setValidator(QDoubleValidator())

        self.underlying_price_label = QLabel("Underlying Price:")
        self.underlying_price_label.setFixedHeight(10)
        self.underlying_price_label.setMaximumHeight(10)
        self.underlying_price_widget = QLineEdit()
        self.underlying_price_widget.setPlaceholderText("Underlying Price")
        self.underlying_price_widget.setValidator(QDoubleValidator())

        self.execution_widget = QDateEdit()
        self.execution_widget.setCalendarPopup(True)
        self.execution_widget.setDisplayFormat("dd-MM-yyyy")
        self.execution_widget.setDate(QDate.currentDate())
        self.execution_label = QLabel("Execution Date:")
        self.execution_label.setFixedHeight(10)
        self.execution_label.setMaximumHeight(10)
        self.execution_layout = QHBoxLayout()
        self.execution_layout.addWidget(self.execution_label)
        self.execution_layout.addWidget(self.execution_widget)

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
    def execution(self):
        return self.execution_widget.date()

    @property
    def expiration(self):
        return self.expiration_widget.date()
