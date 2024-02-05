from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import (
    QDialog,
    QWidget,
    QTableView,
    QPushButton,
)
from PyQt6.QtGui import QIcon

from views.options.addOptionDialog import AddOptionDialog
from views.common.tableViewButtonDelegates import EditDeleteButtonsDelegate


class OptionsTabView(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.repository = parent.repository.option_repository
        self.controller = parent.controller.option_controller
        self.parent = parent

        self.options = QWidget()
        self.options.setObjectName(u"options")
        self.parent.ui.tabWidget.addTab(self, "Options")

        self.setup_table_view()

        self.addButton = AddButton(self)
        self.addButton.clicked.connect(self.show_add_dialog)

    def setup_table_view(self):
        self.optionTableView = QTableView(self)
        self.optionTableView.setObjectName(u"optionTableView")
        self.optionTableView.setGeometry(QRect(0, 0, 800, 600))
        self.optionTableView.setModel(self.repository)
        self.optionTableView.horizontalHeader().setStretchLastSection(True)

        delegate = EditDeleteButtonsDelegate(self.optionTableView)
        self.optionTableView.setItemDelegateForColumn(
            self.repository.columnCount(None)-1, delegate)

    def resizeEvent(self, event):
        self.addButton.resizeEvent(event)

    def show_add_dialog(self):
        dlg = AddOptionDialog(self.controller)
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
