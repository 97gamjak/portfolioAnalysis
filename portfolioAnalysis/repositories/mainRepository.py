from repositories.optionRepository import OptionRepository
from repositories.assetRepository import AssetRepository


class MainRepository:
    def __init__(self, sql_engine):
        self.sql_engine = sql_engine
        self.option_repository = OptionRepository(self.sql_engine)
        self.asset_repository = AssetRepository(self.sql_engine)
