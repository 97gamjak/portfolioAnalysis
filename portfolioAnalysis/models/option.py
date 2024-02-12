from __future__ import annotations

import datetime as dt

from typing import Optional
from sqlmodel import SQLModel, Field

from portfolioAnalysis.enums.optionType import OptionType
from portfolioAnalysis.enums.currency import Currency


class Option(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    option_type: OptionType
    strike_price: float
    premium: float
    currency: Currency

    shares: int = 1

    execution_date: dt.date
    expiration_date: dt.date

    underlying_ticker: str = Field(default=None, foreign_key="asset.ticker")
    underlying_price: Optional[float] = None
    underlying_shares: int = 100

    @property
    def ticker(self):
        return self.underlying_ticker + self._transform_date() + self.option_type.ticker_symbol + self._transform_strike_price()

    def _transform_date(self):
        day = str(self.expiration_date.day).zfill(2)
        month = str(self.expiration_date.month).zfill(2)
        year = str(self.expiration_date.year)[2:]

        return year + month + day

    def _transform_strike_price(self):
        return f"{self.strike_price:.3f}".replace(".", "").zfill(8)

    def edit(self, option: Option):
        self.option_type = option.option_type
        self.strike_price = option.strike_price
        self.expiration_date = option.expiration_date
        self.premium = option.premium
        self.underlying_price = option.underlying_price
        self.underlying_ticker = option.underlying_ticker
        return self

    @property
    def premium_currency_string(self):
        return f"{self.currency} {self.premium}"

    @property
    def strike_price_currency_string(self):
        return f"{self.currency} {self.strike_price}"
