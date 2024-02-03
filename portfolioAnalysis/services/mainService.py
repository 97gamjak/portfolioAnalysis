from services.optionService import OptionService


class MainService:
    def __init__(self, sql_engine, main_repository):
        self.sql_engine = sql_engine
        self.main_repository = main_repository

        self.option_service = OptionService(
            sql_engine, main_repository.option_repository)
