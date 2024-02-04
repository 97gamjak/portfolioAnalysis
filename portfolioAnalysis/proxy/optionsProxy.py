import datetime as dt

from PyQt6.QtCore import QSortFilterProxyModel


class OpenOptionProxy(QSortFilterProxyModel):
    def __init__(self, parent, model):
        super().__init__(parent)
        self.parent = parent
        self.setSourceModel(model)
        self.setFilterKeyColumn(model.expiration_date_column)

    def filterAcceptsRow(self, source_row, source_parent):
        idx = self.sourceModel().index(
            source_row, self.filterKeyColumn(), source_parent)
        data = self.sourceModel().data(idx, self.filterRole())
        return dt.date.fromisoformat(data) >= dt.date.today()


class ClosedOptionProxy(OpenOptionProxy):
    def __init__(self, parent, model):
        super().__init__(parent, model)

    def filterAcceptsRow(self, source_row, source_parent):
        return not super().filterAcceptsRow(source_row, source_parent)
