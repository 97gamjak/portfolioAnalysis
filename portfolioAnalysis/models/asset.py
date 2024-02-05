from sqlmodel import Field, SQLModel
from typing import Optional

from enums.assetType import AssetType


class Asset(SQLModel, table=True):
    ticker: str = Field(primary_key=True)
    sql_asset_type: AssetType = Field(default=AssetType.STOCK)
