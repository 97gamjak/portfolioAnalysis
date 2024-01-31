from PyQt6.QtCore import QObject, pyqtSlot

from models.option import Option


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model


class OptionsTabController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @pyqtSlot(dict)
    def show_add_dialog(self, value):
        option = Option(value)
        print("show_add_dialog")
        print(value)
    # def __init__(self, model):
    #     super().__init__()

    # @pyqtSlot(int)
    # def change_amount(self, value):
    #     self._model.amount = value

    #     # calculate even or odd
    #     self._model.even_odd = 'odd' if value % 2 else 'even'

    #     # calculate button enabled state
    #     self._model.enable_reset = True if value else False
