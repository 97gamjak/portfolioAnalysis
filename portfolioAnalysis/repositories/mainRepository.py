from repositories.optionRepository import OptionRepository


class MainRepository:
    def __init__(self, sql_engine):
        self.sql_engine = sql_engine
        self.option_repository = OptionRepository(self.sql_engine)
