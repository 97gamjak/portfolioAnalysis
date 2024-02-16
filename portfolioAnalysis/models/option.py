from __future__ import annotations

import datetime as dt

from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

from portfolioAnalysis.enums.optionType import OptionType
from portfolioAnalysis.enums.currency import Currency

if TYPE_CHECKING:
    from portfolioAnalysis.models.optionPremium import OptionPremium


class Option(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    option_type: OptionType
    strike_price: float
    premium: float
    currency: Currency
    commission: Optional[float] = 0.0

    shares: int = 1

    execution_date: dt.date
    expiration_date: dt.date

    close_date: Optional[dt.date] = None
    closing_premium: Optional[float] = 0.0
    closing_commission: Optional[float] = 0.0

    underlying_price: Optional[float] = None
    underlying_shares: int = 100
    underlying_ticker: str = Field(default=None, foreign_key="asset.ticker")
    # underlying: Optional["Asset"] = Relationship(
    #     back_populates="asset.options")

    live_premiums: List["OptionPremium"] = Relationship(
        back_populates="option")

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
        self.currency = option.currency
        self.premium = option.premium
        self.strike_price = option.strike_price
        self.commission = option.commission
        self.execution_date = option.execution_date
        self.expiration_date = option.expiration_date
        self.shares = option.shares
        self.underlying_shares = option.underlying_shares
        self.underlying_price = option.underlying_price
        self.underlying_ticker = option.underlying_ticker
        return self

    def close(self, close_option):
        self.close_date = close_option.close_date
        self.closing_premium = close_option.premium
        self.closing_commission = close_option.commission

    @property
    def avg_strike(self):
        return self.strike_price

    @property
    def total_commission(self):
        return self.commission + self.closing_commission

    @property
    def total_premium(self):
        return self.premium - self.total_commission - self.closing_premium

    @property
    def theoretical_yield(self):
        return self.premium / self.strike_price

    @property
    def effective_yield(self):
        return self.total_premium / self.strike_price

    @property
    def theoretical_yearly_yield(self):
        return self.theoretical_yield * 365 / (self.expiration_date - self.execution_date).days

    @property
    def effective_yearly_yield(self):
        return self.effective_yield * 365 / (self.expiration_date - self.execution_date).days

    @property
    def total_days(self):
        return (self.expiration_date - self.execution_date).days

    @property
    def days_to_expiration(self):
        return (self.expiration_date - dt.date.today()).days

    @property
    def actual_days(self):
        return (self.close_date - self.execution_date).days if self.close_date is not None else self.total_days

    @property
    def past_time(self):
        return (dt.date.today() - self.execution_date).days / self.total_days

    @property
    def is_open(self):
        return self.expiration_date >= dt.date.today() if self.close_date is None else False
