from portfolioAnalysis.repositories.optionRepository import OptionRepository
from portfolioAnalysis.repositories.assetRepository import AssetRepository
from portfolioAnalysis.repositories.optionPremiumRepository import OptionPremiumRepository


class MainRepository:
    def __init__(self):
        self.option_repository = OptionRepository()
        self.asset_repository = AssetRepository()
        self.option_premium_repository = OptionPremiumRepository()
