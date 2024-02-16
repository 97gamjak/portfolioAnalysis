from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QDialogButtonBox,
    QLabel,
    QLineEdit,
    QDateEdit,
)
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QDoubleValidator


class CloseOptionDialog(QDialog):
    def __init__(self, controller, index):
        super().__init__()
        self.controller = controller
        self.index = index

        self.setWindowTitle("Close Option")

        self.option = self.controller.get_option(index)
        self.underlying = self.controller.get_underlying_by_option(self.option)

        layout = QVBoxLayout()

        header = QLabel(self.get_header())
        header.setStyleSheet("font-size: 18px; font-weight: bold;")

        layout.addWidget(header)

        button_box = QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(button_box)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.close_option_view = CloseOptionView()
        layout.addLayout(self.close_option_view.layout)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

    def get_header(self):
        return str(self.option.option_type) + " " + self.underlying.company_name + "(" + self.underlying.ticker + ")"

    def accept(self):
        self.controller.close_option(self.close_option_view, self.index)
        super().accept()

    def reject(self):
        super().reject()


class CloseOptionView:
    def __init__(self):
        self.labels = []
        self.widgets = []

        self.premium_label = QLabel("Premium Close Price:")
        self.labels.append(self.premium_label)
        self.premium_widget = self.init_line_edit(
            "Premium Close Price", QDoubleValidator())
        self.widgets.append(self.premium_widget)

        self.commission_label = QLabel("Close Commission:")
        self.labels.append(self.commission_label)
        self.commission_widget = self.init_line_edit(
            "Close Commission", QDoubleValidator(), "0.0")
        self.widgets.append(self.commission_widget)

        self.execution_label = QLabel("Close Date:")
        self.labels.append(self.execution_label)
        self.execution_widget = self.init_qdate_edit()
        self.widgets.append(self.execution_widget)

        self.layout = QVBoxLayout()

        for label in self.labels:
            label.setFixedHeight(10)
            label.setMaximumHeight(10)

        assert len(self.labels) == len(self.widgets)

        for i in range(len(self.labels)):
            self.layout.addWidget(self.labels[i])
            self.layout.addWidget(self.widgets[i])

    def init_line_edit(self, place_holder: str, validator, default_value: str = ""):
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(place_holder)
        line_edit.setValidator(validator)
        line_edit.setText(default_value)
        return line_edit

    def init_qdate_edit(self):
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDisplayFormat("dd-MM-yyyy")
        date_edit.setDate(QDate.currentDate())
        return date_edit

    @property
    def premium(self):
        return self.premium_widget.text()

    @property
    def commission(self):
        return self.commission_widget.text()

    @property
    def close_date(self):
        return self.execution_widget.date()
