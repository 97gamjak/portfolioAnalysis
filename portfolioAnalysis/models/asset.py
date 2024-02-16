from sqlmodel import Field, SQLModel, Relationship
from typing import List

from portfolioAnalysis.enums.assetType import AssetType


class Asset(SQLModel, table=True):
    ticker: str = Field(primary_key=True)
    company_name: str = ""
    sql_asset_type: AssetType = Field(default=AssetType.STOCK)

    # options: List["Option"] = Relationship(back_populates="underlying")
