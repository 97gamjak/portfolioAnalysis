import sys

from PyQt6.QtWidgets import QApplication

from portfolioAnalysis.controllers import MainController
from portfolioAnalysis.repositories import MainRepository
from portfolioAnalysis.views import MainView
from portfolioAnalysis.db import init_db


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
