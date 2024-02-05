from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex
from sqlmodel import Session, select
from datetime import datetime as dt

from models.option import Option
from db import sql_engine


class OptionRepository(QAbstractTableModel):
    headers = ["Ticker", "Premium", ""]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.refresh()

    def rowCount(self, parent):
        return len(self.table)

    def columnCount(self, parent):
        return len(self.table[0]) if len(self.table) > 0 else 0

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

    def get_table_data(self):
        table = []
        for option in self.options:
            table.append(
                [option.ticker, option.premium, ""])

        return table
