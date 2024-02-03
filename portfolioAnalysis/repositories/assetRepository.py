from PyQt6.QtCore import QAbstractTableModel, Qt
from sqlmodel import Session, select

from models.asset import Asset


class AssetRepository(QAbstractTableModel):
    def __init__(self, sql_engine, parent=None):
        super().__init__(parent)
        self.sql_engine = sql_engine
        self.refresh()

    def rowCount(self, parent):
        return len(self.table)

    def columnCount(self, parent):
        return len(self.table[0]) if self.rowCount(parent) > 0 else 0

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
        self.assets = self.get_assets()
        self.table = self.get_table_data()

    def add_asset(self, asset):
        with Session(self.sql_engine) as session:
            session.add(asset)
            session.commit()
            self.refresh()

    def get_assets(self):
        with Session(self.sql_engine) as session:
            try:
                statement = select(Asset)
                return session.exec(statement).all()
            except Exception:
                return []

    def get_table_data(self):
        table = []
        for asset in self.assets:
            table.append(
                [asset.ticker])

        return table

    def find_asset_by_ticker(self, ticker):
        with Session(self.sql_engine) as session:
            try:
                statement = select(Asset).where(Asset.ticker == ticker)
                return session.exec(statement).first()
            except Exception:
                return None

    def create_or_add_asset(self, ticker):
        asset = Asset(ticker=ticker)
        if self.find_asset_by_ticker(asset.ticker) is None:
            self.add_asset(asset)
        return asset
