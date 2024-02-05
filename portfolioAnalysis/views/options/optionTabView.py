from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import (
    QDialog,
    QWidget,
    QTableView,
)

from views.options.addButton import AddButton
from views.options.addButtonDialog import AddButtonDialog
from views.common.tableViewButtonDelegates import EditDeleteButtonsDelegate


class OptionsTabView(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.repository = parent.repository.option_repository
        self.controller = parent.controller.option_controller
        self.parent = parent

        self.options = QWidget()
        self.options.setObjectName(u"options")
        self.parent._ui.tabWidget.addTab(self, "Options")

        self.optionTableView = QTableView(self)
        self.optionTableView.setObjectName(u"optionTableView")
        self.optionTableView.setGeometry(QRect(0, 0, 800, 600))
        self.optionTableView.setModel(self.repository)
        self.optionTableView.horizontalHeader().setStretchLastSection(True)

        delegate = EditDeleteButtonsDelegate(self.optionTableView)
        self.optionTableView.setItemDelegateForColumn(
            self.repository.columnCount(None)-1, delegate)

        self.addButton = AddButton(self)
        self.addButton.clicked.connect(self.show_add_dialog)

    def resizeEvent(self, event):
        self.addButton.resizeEvent(event)

    def show_add_dialog(self):
        dlg = AddButtonDialog(self.controller)
        dlg.exec()
