from sqlmodel import Session


class OptionService:
    def __init__(self, sql_engine, option_repository):
        self.sql_engine = sql_engine
        self.option_repository = option_repository

    def add_option(self, option):
        with Session(self.sql_engine) as session:
            session.add(option)
            session.commit()
            self.option_repository.refresh()
