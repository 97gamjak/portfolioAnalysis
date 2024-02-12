from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
)


class InfoOptionDialog(QDialog):
    def __init__(self, controller, index=None):
        super().__init__()
        self.controller = controller
        self.index = index

        self.setWindowTitle("Option Details")

        self.option = self.controller.get_option(index)
        self.underlying = self.controller.get_underlying_by_option(self.option)

        layout = QVBoxLayout()

        header = QLabel(self.get_header())
        header.setStyleSheet("font-size: 18px; font-weight: bold;")

        layout.addWidget(header)
        self.setLayout(layout)

    def get_header(self):
        return str(self.option.option_type) + " " + self.underlying.company_name + "(" + self.underlying.ticker + ")"
