from PyQt6.QtCore import QRect, QModelIndex, Qt
from PyQt6.QtWidgets import (
    QDialog,
    QWidget,
    QTableView,
    QPushButton,
    QHeaderView,
    QVBoxLayout,
    QProgressDialog,
)
from PyQt6.QtGui import QIcon

from portfolioAnalysis.views.options.addOptionDialog import AddOptionDialog
from portfolioAnalysis.views.options.infoOptionDialog import InfoOptionDialog
from portfolioAnalysis.views.common.tableViewButtonDelegates import EditDeleteButtonsDelegate
from portfolioAnalysis.views.options.closeOptionDialog import CloseOptionDialog
from portfolioAnalysis.proxy.optionsProxy import OpenOptionProxy, ClosedOptionProxy


class OptionsListView(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.repository = parent.repository.option_repository
        self.controller = parent.controller.option_controller
        self.parent = parent

        self.options = QWidget()
        self.options.setObjectName(u"options")

        self.open_option_proxy = OpenOptionProxy(self, self.repository)
        self.closed_option_proxy = ClosedOptionProxy(self, self.repository)
        self.open_option_table_view = self.setup_table_view(
            self.open_option_proxy)
        self.closed_option_table_view = self.setup_table_view(
            self.closed_option_proxy)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.open_option_table_view)
        self.layout.addWidget(self.closed_option_table_view)

        self.setLayout(self.layout)

        self.add_button = AddButton(self)
        self.add_button.clicked.connect(self.show_add_dialog)

        self.update_button = UpdateButton(self)
        self.update_button.clicked.connect(self.update)

    def setup_table_view(self, proxy):
        table_view = QTableView(self)
        table_view.setGeometry(QRect(0, 0, 800, 600))
        table_view.horizontalHeader().setStretchLastSection(True)
        table_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

        table_view.setModel(proxy)

        delegate = EditDeleteButtonsDelegate(
            table_view)
        table_view.setItemDelegateForColumn(
            self.repository.columnCount(None)-1, delegate)

        delegate.delete_button_clicked.connect(
            lambda x: self.delete_option(x, proxy))
        delegate.edit_button_clicked.connect(
            lambda x: self.edit_option(x, proxy))
        delegate.info_button_clicked.connect(
            lambda x: self.info_option(x, proxy))
        delegate.close_button_clicked.connect(
            lambda x: self.close_option(x, proxy))

        return table_view

    def resizeEvent(self, event):
        self.add_button.resizeEvent(event)

    def show_add_dialog(self):
        dlg = AddOptionDialog(self.controller)
        dlg.exec()

    def delete_option(self, index, proxy):
        index = proxy.mapToSource(QModelIndex(index))
        self.controller.delete_option(index.row())

    def edit_option(self, index, proxy):
        index = proxy.mapToSource(QModelIndex(index))
        dlg = AddOptionDialog(self.controller, index.row())
        dlg.exec()

    def info_option(self, index, proxy):
        index = proxy.mapToSource(QModelIndex(index))
        dlg = InfoOptionDialog(self.controller, index.row())
        dlg.exec()

    def close_option(self, index, proxy):
        index = proxy.mapToSource(QModelIndex(index))
        dlg = CloseOptionDialog(self.controller, index.row())
        dlg.exec()

    def update(self):
        dlg = UpdateDialog(
            self.controller, self.parent.repository.option_premium_repository)
        dlg.exec()


class AddButton(QPushButton):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setIcon(QIcon.fromTheme("list-add"))
        self.setStyleSheet(
            "background-color: green; border: 1px solid #d3d3d3; border-radius: 5px;")
        self.delta_x = 100
        self.delta_y = 60
        x = parent.width() - self.delta_x
        y = parent.height() - self.delta_y
        super().setGeometry(QRect(x, y, 40, 24))

        self.parent = parent

    def resizeEvent(self, event):
        new_x = self.parent.width() - self.delta_x
        new_y = self.parent.height() - self.delta_y
        super().move(new_x, new_y)


class UpdateDialog(QProgressDialog):
    def __init__(self, controller, repository):
        super().__init__("Updating option premiums...", "Cancel", 0, 0)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.controller = controller
        self.repository = repository
        self.setGeometry(QRect(0, 0, 800, 100))
        self.setAutoClose(True)

    def exec(self):
        self.show()
        self.repository.maximum_progress.connect(self.set_maximum)
        self.repository.progress.connect(self.set_value)

        self.controller.update()

    def set_maximum(self, value):
        self.setMaximum(value)

    def set_value(self, value):
        self.setValue(value)


class UpdateButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setIcon(QIcon.fromTheme("view-refresh"))
        self.setStyleSheet(
            "background-color: blue; border: 1px solid #d3d3d3; border-radius: 5px;")
        self.delta_x = 160
        self.delta_y = 60
        x = parent.width() - self.delta_x
        y = parent.height() - self.delta_y
        super().setGeometry(QRect(x, y, 40, 24))

        self.parent = parent

    def resizeEvent(self, event):
        new_x = self.parent.width() - self.delta_x
        new_y = self.parent.height() - self.delta_y
        super().move(new_x, new_y)
