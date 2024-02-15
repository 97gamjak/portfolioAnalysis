from enum import Enum


class Currency(Enum):
    USD = "$"
    EUR = "€"

    def __str__(self):
        return self.value

    @classmethod
    def values(cls):
        return [currency.value for currency in Currency]

    def transform(self, value):
        return self.value + "{:,.2f}".format(value)
