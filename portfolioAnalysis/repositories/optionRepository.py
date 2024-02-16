from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex
from sqlmodel import Session, select
from datetime import datetime as dt

from portfolioAnalysis.models.option import Option
from portfolioAnalysis.db import sql_engine


class OptionRepository(QAbstractTableModel):
    headers = ["Ticker", "Premium", "Strike",
               "Execution Date", "Expiration Date", "Shares", "Underlying Shares", ""]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.refresh()

    def rowCount(self, parent):
        return len(self.table)

    def columnCount(self, parent):
        return len(self.headers)

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.headers[section]
            else:
                return section + 1

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            column = index.column()
            return self.table[row][column]

    def refresh(self):
        self.options = self.get_options()
        self.table = self.get_table_data()

    def add_option(self, option):
        with Session(sql_engine) as session:
            session.add(option)
            session.commit()
            session.refresh(option)
            self.beginInsertRows(QModelIndex(), self.rowCount(
                self.parent), self.rowCount(self.parent))
            self.refresh()
            self.endInsertRows()

    def get_options(self):
        with Session(sql_engine) as session:
            try:
                statement = select(Option)
                return session.exec(statement).all()
            except Exception:
                return []

    def get_open_options(self):
        self.options = self.get_options()
        return [option for option in self.options if option.is_open]

    def get_closed_options(self):
        self.options = self.get_options()
        return [option for option in self.options if not option.is_open]

    def get_table_data(self):
        table = []
        for option in self.options:
            currency = option.currency
            table.append(
                [option.ticker,
                 currency.transform(option.premium),
                 currency.transform(option.strike_price),
                 str(option.execution_date),
                 str(option.expiration_date),
                 option.shares,
                 option.underlying_shares,
                 ""
                 ])

        return table

    def delete_option_by_index(self, index):
        with Session(sql_engine) as session:
            session.delete(self.options[index])
            session.commit()
            self.beginRemoveRows(QModelIndex(), index, index)
            self.refresh()
            self.endRemoveRows()

    def get_option_by_index(self, index):
        return self.options[index]

    def edit_option(self, option, index):
        with Session(sql_engine) as session:
            option_to_edit = self.find_option_by_index(index)
            option_to_edit.edit(option)
            session.add(option_to_edit)
            session.commit()
            session.refresh(option_to_edit)
            self.refresh()
            self.dataChanged.emit(self.index(index, 0), self.index(
                index, self.columnCount(self.parent)))

    def close_option(self, option, close_option):
        with Session(sql_engine) as session:
            option_to_close = self.find_option_by_option(option)
            option_to_close.close(close_option)
            session.add(option_to_close)
            session.commit()
            session.refresh(option_to_close)
            self.refresh()

    def find_option_by_option(self, option):
        with Session(sql_engine) as session:
            statement = select(Option).where(Option.id == option.id)
            return session.exec(statement).first()

    def find_option_by_index(self, index):
        with Session(sql_engine) as session:
            option = self.options[index]
            statement = select(Option).where(Option.id == option.id)
            return session.exec(statement).first()

    @property
    def expiration_date_column(self):
        return self.headers.index("Expiration Date")
