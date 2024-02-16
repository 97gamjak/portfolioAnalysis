import datetime as dt

from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from portfolioAnalysis.models.option import Option


class OptionPremium(SQLModel, table=True):
    premium: float
    date: dt.date = Field(primary_key=True)

    option_id: int = Field(foreign_key="option.id", primary_key=True)
    option: "Option" = Relationship(back_populates="live_premiums")
