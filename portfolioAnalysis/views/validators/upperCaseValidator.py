from PyQt6.QtGui import QValidator


class UpperCaseValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, string, pos):
        return QValidator.State.Acceptable, string.upper(), pos
