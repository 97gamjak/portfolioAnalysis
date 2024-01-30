import sys
from PyQt6.QtWidgets import QApplication

from controllers.main_controller import MainController
from models.model import Model
from views.main_view import MainView


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        self.model = Model()
        self.main_controller = MainController(self.model)
        self.main_view = MainView(self.model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
