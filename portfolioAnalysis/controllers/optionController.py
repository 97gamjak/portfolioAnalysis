import yfinance as yf
import requests

from PyQt6.QtCore import pyqtSlot, pyqtSignal, QObject
from PyQt6.QtWidgets import QLayout

from models.option import Option
from enums.optionType import OptionType


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
        underlying_ticker = option_view.ticker

        validate_not_empty(option_view.strike, "Strike")
        validate_not_empty(option_view.premium, "Premium")
        strike = float(option_view.strike)
        premium = float(option_view.premium)

        option_type = OptionType(option_view.option_type)
        expiration = option_view.expiration.toPyDate()
        execution = option_view.execution.toPyDate()

        underlying_price = option_view.underlying_price if option_view.underlying_price else None

        option = Option(
            option_type=option_type,
            underlying_ticker=underlying_ticker,
            strike_price=strike,
            expiration_date=expiration,
            execution_date=execution,
            premium=premium,
            underlying_price=underlying_price
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

        print(response["quotes"][0]["symbol"])

        if response["quotes"][0]["symbol"] != ticker:
            ambiguous_tickers = [quote["symbol"] + " " + quote["shortname"]
                                 for quote in response["quotes"]]
            self.ambiguous_ticker.emit(ambiguous_tickers)


def validate_not_empty(value, message):
    if not value:
        raise ValueError(f"{message} can not be empty")


url = 'https://query2.finance.yahoo.com/v1/finance/search'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
}


def params_init(text: str):
    params = {}
    params["q"] = text
    params["quotesCount"] = 10
    params["newsCount"] = 0
    params["enableFuzzyQuery"] = False
    params["quotesQueryId"] = "tss_match_phrase_query"

    return params
