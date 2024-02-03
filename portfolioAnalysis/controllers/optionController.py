import datetime as dt

from PyQt6.QtCore import pyqtSlot, pyqtSignal, QObject
from PyQt6.QtWidgets import QLayout

from models.option import Option


class OptionController(QObject):
    add_option_successful = pyqtSignal()

    def __init__(self, service):
        super().__init__()
        self.service = service

    def add_option(self, add_option_view):
        try:
            if not add_option_view.ticker:
                raise ValueError("Ticker is required")

            ticker = add_option_view.ticker
            strike = float(add_option_view.strike)
            expiration = dt.strptime(
                add_option_view.expiration, "%d-%m-%Y").date()
            premium = float(add_option_view.premium)

            option = Option(ticker=ticker, strike_price=strike,
                            expiration_date=expiration, premium=premium)

            self.service.add_option(option)
        except Exception:
            self.add_option_successful.emit()
