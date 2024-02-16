from portfolioAnalysis.models.asset import Asset


class OptionService:
    def __init__(self, repository):
        self.option_repository = repository.option_repository
        self.asset_repository = repository.asset_repository
        self.option_premium_repository = repository.option_premium_repository

    def delete_option(self, index):
        option_id = self.get_option(index).id
        self.option_repository.delete_option_by_index(index)
        self.option_premium_repository.delete_option_premium_by_id(option_id)

    def get_option(self, index):
        return self.option_repository.get_option_by_index(index)

    def get_options(self):
        return self.option_repository.get_options()

    def get_open_options(self):
        return self.option_repository.get_open_options()

    def get_closed_options(self):
        return self.option_repository.get_closed_options()

    def add_option(self, option):

        asset = Asset(ticker=option.underlying_ticker)

        self.asset_repository.create_asset_if_not_found(asset)
        self.option_repository.add_option(option)
        self.option_premium_repository.add_initial_option_premium_by_option(
            option)

    def edit_option(self, option, index):
        asset = Asset(ticker="test", test=1)

        self.asset_repository.create_asset_if_not_found(asset)
        self.option_repository.edit_option(option, index)
        option = self.get_option(index)
        self.option_premium_repository.change_initial_option_premium_by_option(
            option)

    def get_underlying_by_option(self, option):
        return self.asset_repository.find_asset_by_ticker(
            option.underlying_ticker)

    def get_option_premiums_by_option(self, option):
        return self.option_premium_repository.get_option_premiums_by_option(option)

    def update(self):
        self.option_premium_repository.update()
