from PyQt6.QtCore import pyqtSlot, pyqtSignal, QObject
from PyQt6.QtWidgets import QLayout

from models.option import Option


class OptionController(QObject):
    add_option_successful = pyqtSignal(bool)

    def __init__(self, service):
        super().__init__()
        self.service = service

    def add_option(self, add_option_view):
        try:
            if not add_option_view.ticker:
                raise ValueError("Ticker is required")

            ticker = add_option_view.ticker
            strike = float(add_option_view.strike)
            expiration = add_option_view.expiration.toPyDate()
            premium = float(add_option_view.premium)

            option = Option(ticker=ticker, strike_price=strike,
                            expiration_date=expiration, premium=premium)

            self.service.add_option(option)
            self.add_option_successful.emit(True)
        except Exception as e:
            print(e)
            self.add_option_successful.emit(False)
