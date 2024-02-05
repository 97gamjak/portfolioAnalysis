from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QComboBox,
    QVBoxLayout,
)


class AmbiguousTickerDialog(QDialog):
    def __init__(self, ambiguous_tickers):
        super().__init__()

        self.ticker = None

        self.combo_box = QComboBox()
        self.combo_box.setGeometry(QRect(0, 0, 1000, 200))
        self.combo_box.addItems(ambiguous_tickers)
        self.combo_box.show()

        button_box = QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(button_box)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept(self):
        self.ticker = self.combo_box.currentText().split(" ")[0]
        super().accept()
