import yfinance as yf
import requests

from PyQt6.QtCore import pyqtSlot, pyqtSignal, QObject
from PyQt6.QtWidgets import QLayout

from models.option import Option
from enums.optionType import OptionType
from utils.yfinanceUtils import params_init, url, headers


class OptionController(QObject):
    add_option_successful = pyqtSignal(bool, str)
    ambiguous_ticker = pyqtSignal(list)
    invalid_ticker = pyqtSignal()

    def __init__(self, service):
        super().__init__()
        self.service = service

    def delete_option(self, index):
        self.service.delete_option(index)

    def get_option(self, index):
        return self.service.get_option(index)

    def add_option(self, option_view):
        try:
            option = self.translate_option_view(option_view)

            self.service.add_option(option)
            self.add_option_successful.emit(True, "OK")
        except Exception as e:
            self.add_option_successful.emit(False, str(e))

    def edit_option(self, option_view, index):
        try:
            option = self.translate_option_view(option_view)

            self.service.edit_option(option, index)
            self.add_option_successful.emit(True, "OK")
        except Exception as e:
            self.add_option_successful.emit(False, str(e))

    def translate_option_view(self, option_view):
        validate_not_empty(option_view.strike, "Strike")
        validate_not_empty(option_view.premium, "Premium")

        option = Option(
            option_type=OptionType(option_view.option_type),
            underlying_ticker=option_view.ticker,
            strike_price=float(option_view.strike),
            expiration_date=option_view.expiration_date.toPyDate(),
            execution_date=option_view.execution_date.toPyDate(),
            premium=float(option_view.premium),
            shares=int(option_view.shares) if option_view.shares else 1,
            underlying_price=float(
                option_view.underlying_price) if option_view.underlying_price else None,
            underlying_shares=int(
                option_view.underlying_shares) if option_view.underlying_shares else 100
        )

        return option

    def validate_ticker(self, ticker):
        if not ticker:
            self.invalid_ticker.emit()
            return

        params = params_init(ticker)
        response = requests.get(url, headers=headers, params=params).json()

        if not response["quotes"]:
            self.invalid_ticker.emit()
            return

        if response["quotes"][0]["symbol"] != ticker:
            ambiguous_tickers = [quote["symbol"] + " " + quote["shortname"]
                                 for quote in response["quotes"]]
            self.ambiguous_ticker.emit(ambiguous_tickers)


def validate_not_empty(value, message):
    if not value:
        raise ValueError(f"{message} can not be empty")
