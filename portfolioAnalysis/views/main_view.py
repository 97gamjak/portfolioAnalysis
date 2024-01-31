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
)
from PyQt6.QtGui import QDoubleValidator
from PyQt6.uic import loadUi

from __init__ import __resources_path__

from controllers.main_controller import MainController, OptionsTabController
import resources.resources


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._ui = loadUi(__resources_path__ / "main_view.ui", self)
        self._model = model
        self._main_controller = main_controller
        self._options_tab = OptionsTab(self, model)

    def resizeEvent(self, event):
        self._options_tab.resizeEvent(event)


class OptionsTab(QDialog):
    def __init__(self, parent, main_model):
        super().__init__(parent)
        self.controller = OptionsTabController(main_model)

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

        self.option_type = QComboBox()
        self.option_type.addItem("Put Sell")
        self.option_type.addItem("Call Sell")
        self.option_type.addItem("Put Buy")
        self.option_type.addItem("Call Buy")

        self.ticker = QLineEdit()
        self.ticker.setPlaceholderText("Ticker")

        self.underlying = QLineEdit()
        self.underlying.setPlaceholderText("Underlying")

        self.strike = QLineEdit()
        self.strike.setPlaceholderText("Strike")
        self.strike.setValidator(QDoubleValidator())

        self.expiration = QDateEdit()
        self.expiration.setCalendarPopup(True)
        self.expiration.setDisplayFormat("dd-MM-yyyy")
        self.expiration.setDate(QDate.currentDate())
        self.expiration_label = QLabel("Expiration Date:")
        self.expiration_label.setFixedHeight(10)
        self.expiration_label.setMaximumHeight(10)

        self.expiration_layout = QHBoxLayout()
        self.expiration_layout.addWidget(self.expiration_label)
        self.expiration_layout.addWidget(self.expiration)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.option_type)
        self.layout.addWidget(self.ticker)
        self.layout.addWidget(self.underlying)
        self.layout.addWidget(self.strike)
        self.layout.addLayout(self.expiration_layout)
        self.layout.addWidget(self.expiration)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.buttonBox.accepted.connect(
            lambda: self.controller.show_add_dialog(self.ticker.text()))

    def accept(self):
        signal = {
            "ticker": self.ticker.text(),
            "strike": float(self.strike.text()),
            "expiration": self.expiration.text(),
            "price": 0.0,
        }

        self.controller.show_add_dialog(signal)

    # # connect widgets to controller
    # self._ui.spinBox_amount.valueChanged.connect(
    #     self._main_controller.change_amount)
    # self._ui.pushButton_reset.clicked.connect(
    #     lambda: self._main_controller.change_amount(0))

    # listen for model event signals
    # self._model.amount_changed.connect(self.on_amount_changed)
    # self._model.even_odd_changed.connect(self.on_even_odd_changed)
    # self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

    # # set a default value
    # self._main_controller.change_amount(42)

    # @pyqtSlot(int)
    # def on_amount_changed(self, value):
    #     self._ui.spinBox_amount.setValue(value)

    # @pyqtSlot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)

    # @pyqtSlot(bool)
    # def on_enable_reset_changed(self, value):
    #     self._ui.pushButton_reset.setEnabled(value)
