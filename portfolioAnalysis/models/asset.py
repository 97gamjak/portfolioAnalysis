from sqlmodel import Field, SQLModel
from typing import Optional

from enums.assetType import AssetType


class Asset(SQLModel, table=True):
    test: int = Field(primary_key=True)
    ticker: str

    # sql_asset_type: str = Field(default=str(AssetType.STOCK))

    # # @property
    # # def asset_type(self):
    # #     return AssetType(self.sql_asset_type)
    # # @asset_type.setter
    # # def asset_type(self, value):
    # #     self.sql_asset_type = str(value)
    # def __hash__(self):
    #     return hash(self.ticker)
