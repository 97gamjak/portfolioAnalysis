from PyQt6.QtWidgets import (
    QDialog,
)


class InfoOptionDialog(QDialog):
    def __init__(self, controller, index=None):
        super().__init__()
        self.controller = controller
        self.index = index

        self.setWindowTitle("Option Details")

        self.option = self.controller.get_option(index)
