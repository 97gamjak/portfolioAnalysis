from PyQt6.QtCore import QObject

from controllers.optionController import OptionController
from services.mainService import MainService


class MainController(QObject):
    def __init__(self, sql_engine, main_repository):
        super().__init__()

        self.main_service = MainService(main_repository)
        self.option_controller = OptionController(
            self.main_service.option_service)
