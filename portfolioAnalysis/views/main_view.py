from PyQt6.QtCore import QObject, QRect, QDate, QPersistentModelIndex
from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QDialog,
    QWidget,
    QVBoxLayout,
    QLabel,
    QDialogButtonBox,
    QTabWidget,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QHBoxLayout,
    QLayout,
    QErrorMessage,
    QMessageBox,
    QTableView,
    QTableWidget,
    QStyledItemDelegate,
)
from PyQt6.QtGui import QDoubleValidator, QValidator, QIcon
from PyQt6.uic import loadUi

from __init__ import __resources_path__
from enums.optionType import OptionType

from views.options.optionTabView import OptionsTabView


class MainView(QMainWindow):
    def __init__(self, repository, controller):
        super().__init__()

        self.repository = repository
        self.controller = controller

        self._ui = loadUi(__resources_path__ / "main_view.ui", self)
        self._options_tab = OptionsTabView(self)

    def resizeEvent(self, event):
        self._options_tab.resizeEvent(event)
