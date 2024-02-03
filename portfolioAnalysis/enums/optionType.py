from enum import Enum


class OptionType(Enum):
    PUT_SELL = "PUT SELL"
    PUT_BUY = "PUT BUY"
    CALL_SELL = "CALL SELL"
    CALL_BUY = "CALL BUY"

    def __str__(self):
        return self.value

    @classmethod
    def values(cls):
        return [option_type.value for option_type in OptionType]

    @property
    def is_call(self):
        return self in [OptionType.CALL_BUY, OptionType.CALL_SELL]

    @property
    def is_put(self):
        return self in [OptionType.PUT_BUY, OptionType.PUT_SELL]

    @property
    def ticker_symbol(self):
        if self.is_call:
            return "C"
        elif self.is_put:
            return "P"
