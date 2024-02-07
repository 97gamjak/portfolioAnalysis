from PyQt6.QtCore import QPersistentModelIndex, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QStyledItemDelegate,
)
from PyQt6.QtGui import QIcon


class ViewWidget(QWidget):
    delete_clicked = pyqtSignal(QPersistentModelIndex)
    edit_clicked = pyqtSignal(QPersistentModelIndex)

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
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        self.content_button.move(x, 0)

        self.delete_button.clicked.connect(self.delete_button_clicked)
        self.edit_button.clicked.connect(self.edit_button_clicked)

    def delete_button_clicked(self):
        emit_index = self.p_index
        self.delete_clicked.emit(emit_index)

    def edit_button_clicked(self):
        emit_index = self.p_index
        self.edit_clicked.emit(emit_index)


class EditDeleteButtonsDelegate(QStyledItemDelegate):
    delete_button_clicked = pyqtSignal(QPersistentModelIndex)
    edit_button_clicked = pyqtSignal(QPersistentModelIndex)

    def paint(self, painter, option, index):
        self.parent().openPersistentEditor(index)
        super().paint(painter, option, index)

    def createEditor(self, parent, option, index):
        self.widget = ViewWidget(0, index, parent)
        self.widget.edit_clicked.connect(self.edit_button_clicked)
        self.widget.delete_clicked.connect(self.delete_button_clicked)
        return self.widget
