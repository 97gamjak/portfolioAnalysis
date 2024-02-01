import datetime as dt

from typing import Optional
from sqlmodel import SQLModel, Field


class Option(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ticker: str
    premium: float
    strike_price: float
    expiration_date: dt.datetime
    underlying_price: Optional[float] = None
