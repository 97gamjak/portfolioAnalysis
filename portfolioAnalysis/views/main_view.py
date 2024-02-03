from PyQt6.QtCore import QRect, QDate
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
)
from PyQt6.QtGui import QDoubleValidator
from PyQt6.uic import loadUi

from __init__ import __resources_path__


class MainView(QMainWindow):
    def __init__(self, repository, controller):
        super().__init__()

        self.repository = repository
        self.controller = controller

        self._ui = loadUi(__resources_path__ / "main_view.ui", self)
        self._options_tab = OptionsTab(self)

    def resizeEvent(self, event):
        self._options_tab.resizeEvent(event)


class OptionsTab(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.repository = parent.repository
        self.controller = parent.controller.option_controller
        self.parent = parent

        self.options = QWidget()
        self.options.setObjectName(u"options")
        self.parent._ui.tabWidget.addTab(self, "Options")

        self._addButton = AddButton(self)
        self._addButton.clicked.connect(self.show_add_dialog)

    def resizeEvent(self, event):
        self._addButton.resizeEvent(event)

    def show_add_dialog(self):
        dlg = AddButtonDialog(self.controller)
        dlg.exec()


class AddButton(QPushButton):

    def __init__(self, parent):
        super().__init__("Add", parent=parent)
        self.delta_x = 100
        self.delta_y = 60
        x = parent.width() - self.delta_x
        y = parent.height() - self.delta_y
        super().setGeometry(QRect(x, y, 80, 24))

        self.parent = parent

    def resizeEvent(self, event):
        new_x = self.parent.width() - self.delta_x
        new_y = self.parent.height() - self.delta_y
        super().move(new_x, new_y)


class AddButtonDialog(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("HELLO!")

        button_box = QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(button_box)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.add_option_view = AddOptionView()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.add_option_view.option_type_widget)
        self.layout.addWidget(self.add_option_view.ticker_widget)
        self.layout.addWidget(self.add_option_view.premium_widget)
        self.layout.addWidget(self.add_option_view.strike_widget)
        self.layout.addWidget(self.add_option_view.underlying_price_widget)
        self.layout.addLayout(self.add_option_view.expiration_layout)
        self.layout.addWidget(self.add_option_view.expiration_widget)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.buttonBox.accepted.connect(self.add_option)
        self.controller.add_option_successful.connect(self.save_error)

    def add_option(self):
        self.controller.add_option(self.add_option_view)
        self.connectNotify

    def save_error(self):
        self.error_box = QErrorMessage()
        self.error_box.showMessage("Error adding option")
        self.error_box.exec()


class AddOptionView:
    def __init__(self):
        self.option_type_widget = QComboBox()
        self.option_type_widget.addItem("Put Sell")
        self.option_type_widget.addItem("Call Sell")
        self.option_type_widget.addItem("Put Buy")
        self.option_type_widget.addItem("Call Buy")

        self.ticker_widget = QLineEdit()
        self.ticker_widget.setPlaceholderText("Ticker")

        self.premium_widget = QLineEdit()
        self.premium_widget.setPlaceholderText("Premium")
        self.premium_widget.setValidator(QDoubleValidator())

        self.strike_widget = QLineEdit()
        self.strike_widget.setPlaceholderText("Strike Price")
        self.strike_widget.setValidator(QDoubleValidator())

        self.underlying_price_widget = QLineEdit()
        self.underlying_price_widget.setPlaceholderText("Underlying Price")
        self.underlying_price_widget.setValidator(QDoubleValidator())

        self.expiration_widget = QDateEdit()
        self.expiration_widget.setCalendarPopup(True)
        self.expiration_widget.setDisplayFormat("dd-MM-yyyy")
        self.expiration_widget.setDate(QDate.currentDate())
        self.expiration_label = QLabel("Expiration Date:")
        self.expiration_label.setFixedHeight(10)
        self.expiration_label.setMaximumHeight(10)

        self.expiration_layout = QHBoxLayout()
        self.expiration_layout.addWidget(self.expiration_label)
        self.expiration_layout.addWidget(self.expiration_widget)

    @property
    def ticker(self):
        return self.ticker_widget.text()

    @property
    def premium(self):
        return self.premium_widget.text()

    @property
    def strike(self):
        return self.strike_widget.text()

    @property
    def underlying_price(self):
        return self.underlying_price_widget.text()

    @property
    def expiration(self):
        return self.expiration_widget.date()
