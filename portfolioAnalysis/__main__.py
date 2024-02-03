import sys

from sqlmodel import create_engine, SQLModel
from PyQt6.QtWidgets import QApplication

from controllers.mainController import MainController
from repositories.mainRepository import MainRepository
from views.main_view import MainView
from models import *  # for SQLModel.metadata.create_all

from __init__ import __resources_path__


def init_db():
    engine = create_engine(
        f"sqlite:///{__resources_path__ / 'portfolio.db'}")
    SQLModel.metadata.create_all(engine)

    return engine


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        self.sql_engine = init_db()
        self.repository = MainRepository(self.sql_engine)
        self.controller = MainController(self.sql_engine, self.repository)
        self.view = MainView(self.repository, self.controller)
        self.view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
