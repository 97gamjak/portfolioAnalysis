from models.asset import Asset


class OptionService:
    def __init__(self, repository):
        self.option_repository = repository.option_repository
        self.asset_repository = repository.asset_repository

    def delete_option(self, index):
        self.option_repository.delete_option_by_index(index)

    def get_option(self, index):
        return self.option_repository.get_option_by_index(index)

    def add_option(self, option):

        asset = Asset(ticker="test", test=1)

        self.asset_repository.create_asset_if_not_found(asset)
        self.option_repository.add_option(option)

    def edit_option(self, option, index):
        asset = Asset(ticker="test", test=1)

        self.asset_repository.create_asset_if_not_found(asset)
        self.option_repository.edit_option(option, index)
