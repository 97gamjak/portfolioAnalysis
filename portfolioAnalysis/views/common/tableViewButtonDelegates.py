from PyQt6.QtCore import QPersistentModelIndex
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QStyledItemDelegate,
)
from PyQt6.QtGui import QIcon


class ViewWidget(QWidget):
    def __init__(self, x, index, parent=None):
        super().__init__(parent)
        self.p_index = QPersistentModelIndex(index)
        self.content_button = QWidget(self)
        layout = QHBoxLayout(self.content_button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.edit_button = QPushButton()
        self.edit_button.setIcon(QIcon.fromTheme("document-edit"))
        self.delete_button = QPushButton()
        self.delete_button.setIcon(QIcon.fromTheme("edit-delete"))
        self.delete_button.setStyleSheet(
            "background-color: red; border: 1px solid #d3d3d3; border-radius: 5px;")
        # self.delete_btn.clicked.connect(self.delete_clicked)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        self.content_button.move(x, 0)


class EditDeleteButtonsDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        self.parent().openPersistentEditor(index)
        super().paint(painter, option, index)

    def createEditor(self, parent, option, index):
        return ViewWidget(0, index, parent)
