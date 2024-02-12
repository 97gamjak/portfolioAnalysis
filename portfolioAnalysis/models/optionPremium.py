from __future__ import annotations

import datetime as dt

from sqlmodel import SQLModel, Field


class OptionPremium(SQLModel, table=True):
    option_id: int = Field(foreign_key="option.id", primary_key=True)
    premium: float
    date: dt.date = Field(primary_key=True)
