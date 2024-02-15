from portfolioAnalysis.services.optionService import OptionService


class MainService:
    def __init__(self, main_repository):
        self.main_repository = main_repository

        self.option_service = OptionService(main_repository)
