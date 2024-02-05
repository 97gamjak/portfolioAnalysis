from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from __init__ import __resources_path__

from views.options.optionTabView import OptionsTabView


class MainView(QMainWindow):
    def __init__(self, repository, controller):
        super().__init__()

        self.repository = repository
        self.controller = controller

        self.ui = loadUi(__resources_path__ / "main_view.ui", self)
        self.options_tab = OptionsTabView(self)

    def resizeEvent(self, event):
        self.options_tab.resizeEvent(event)
