import datetime as dt

from typing import Optional
from sqlmodel import SQLModel, Field

from enums.optionType import OptionType


class Option(SQLModel, table=True):
    option_type: OptionType = Field(primary_key=True)
    strike_price: float = Field(primary_key=True)
    expiration_date: dt.datetime = Field(primary_key=True)
    premium: float

    # underlying_price: Optional[float] = None

    # underlying_ticker: str = Field(
    #     default=None, foreign_key="asset.ticker")

    @property
    def ticker(self):
        return self.underlying_ticker + self._transform_date() + self.option_type.ticker_symbol + self._transform_strike_price()

    def _transform_date(self):
        day = str(self.expiration_date.day).zfill(2)
        month = str(self.expiration_date.month).zfill(2)
        year = str(self.expiration_date.year)[2:]

        return day + month + year

    def _transform_strike_price(self):
        return f"{self.strike_price:.3f}".replace(".", "").zfill(8)
