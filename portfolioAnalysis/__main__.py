import sys

from PyQt6.QtWidgets import QApplication

from controllers.mainController import MainController
from repositories.mainRepository import MainRepository
from views.main_view import MainView

from db import init_db
from models.asset import Asset
from models.option import Option

from __init__ import __resources_path__


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        init_db()
        self.repository = MainRepository()
        self.controller = MainController(self.repository)
        self.view = MainView(self.repository, self.controller)
        self.view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
