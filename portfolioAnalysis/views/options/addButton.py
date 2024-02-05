from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import (
    QPushButton,
)
from PyQt6.QtGui import QIcon


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
