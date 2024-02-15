import sys

from PyQt6.QtWidgets import QApplication

from controllers.mainController import MainController
from repositories.mainRepository import MainRepository
from views.mainView import MainView

from db import init_db


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        init_db()
        self.repository = MainRepository()
        self.controller = MainController(self.repository)
        self.view = MainView(self.repository, self.controller)
        self.view.showMaximized()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
