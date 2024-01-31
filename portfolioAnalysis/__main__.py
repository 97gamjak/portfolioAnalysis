import sys
from PyQt6.QtWidgets import QApplication

from controllers.main_controller import MainController
from models.main_model import MainModel
from views.main_view import MainView

from __init__ import __resources_path__


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        self.main_model = MainModel()
        self.main_controller = MainController(self.main_model)
        self.main_view = MainView(self.main_model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
