from models.asset import Asset


class OptionService:
    def __init__(self, repository):
        self.option_repository = repository.option_repository
        self.asset_repository = repository.asset_repository

    def add_option(self, option):

        asset = Asset(ticker="test", test=1)

        self.asset_repository.create_or_add_asset(asset)
        # self.option_repository.add_option(option)
