from PyQt6.QtCore import QAbstractListModel, Qt
from sqlmodel import Session, select

from models.option import Option


class OptionRepository(QAbstractListModel):
    def __init__(self, sql_engine, parent=None):
        super().__init__(parent)
        self.sql_engine = sql_engine
        self.refresh()

    def rowCount(self, parent):
        return len(self.options)

    def refresh(self):
        self.options = self.get_options()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            option = self.options[index.row()]
            return f"{option.ticker} {option.premium} {option.expiration_date} {option.strike_price}"

    def get_options(self):
        with Session(self.sql_engine) as session:
            try:
                statement = select(Option)
                return session.exec(statement).all()
            except Exception:
                return []
