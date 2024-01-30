import datetime as dt

from dataclasses import dataclass


@dataclass
class Option:
    ticker: str
    strike: float
    expiration: str
    price: float

    def __post_init__(self):
        print(self.ticker, self.strike, self.expiration, self.price)
