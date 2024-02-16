import datetime as dt

from PyQt6.QtCore import QSortFilterProxyModel


class OpenOptionProxy(QSortFilterProxyModel):
    def __init__(self, parent, model):
        super().__init__(parent)
        self.setSourceModel(model)
        model.dataChanged.connect(self.invalidateFilter)

    def filterAcceptsRow(self, source_row, source_parent):
        option = self.sourceModel().options[source_row]
        return option.is_open


class ClosedOptionProxy(OpenOptionProxy):
    def __init__(self, parent, model):
        super().__init__(parent, model)

    def filterAcceptsRow(self, source_row, source_parent):
        return not super().filterAcceptsRow(source_row, source_parent)
