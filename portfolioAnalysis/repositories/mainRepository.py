from repositories.optionRepository import OptionRepository
from repositories.assetRepository import AssetRepository


class MainRepository:
    def __init__(self):
        self.option_repository = OptionRepository()
        self.asset_repository = AssetRepository()
