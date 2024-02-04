from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QMenu,
    QTreeWidget,
    QTreeWidgetItem,
    QLabel,
)

from PyQt6.QtCore import Qt

from views.options.optionListView import OptionsListView


class MainView(QMainWindow):
    def __init__(self, repository, controller):
        super().__init__()

        self.repository = repository
        self.controller = controller

        self.setWindowTitle("Portfolio Analysis")

        self.init_views()
        self.create_menu_bar()
        self.create_side_bar()
        self.init_ui()

        self.tree.itemClicked.connect(self.on_item_clicked)

    def resizeEvent(self, event):
        self.options_view.resizeEvent(event)

    def init_ui(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.tree)
        self.main_layout.addWidget(self.overview_view)

        self.main_layout.setAlignment(self.tree, Qt.AlignmentFlag.AlignLeft)
        self.main_layout.setStretch(1, 1)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = QMenu("&File", self)
        edit_menu = QMenu("&Edit", self)
        help_menu = QMenu("&Help", self)
        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(edit_menu)
        menu_bar.addMenu(help_menu)

    def create_side_bar(self):
        self.tree = QTreeWidget(self)
        self.tree.setHeaderHidden(True)
        self.tree.setFixedWidth(150)

        overview = QTreeWidgetItem(self.tree)
        overview.setText(0, "Overview")

        option = QTreeWidgetItem(self.tree)
        option.setText(0, "Options")

        minor_action1 = QTreeWidgetItem(overview)
        minor_action1.setText(0, "Minor Action 1")

        minor_action2 = QTreeWidgetItem(overview)
        minor_action2.setText(0, "Minor Action 2")

        minor_action3 = QTreeWidgetItem(option)
        minor_action3.setText(0, "Minor Action 3")

        minor_action4 = QTreeWidgetItem(option)
        minor_action4.setText(0, "Minor Action 4")

        self.tree.expandAll()  # Expand all items

    def init_views(self):
        self.views = {}

        self.overview_view = QLabel("Overview")
        self.views["overview"] = self.overview_view

        self.options_view = OptionsListView(self)
        self.views["options"] = self.options_view

        for view in self.views.values():
            view.hide()

        self.overview_view.show()

    def on_item_clicked(self, item, column):

        for view in self.views.values():
            view.hide()
            self.main_layout.removeWidget(view)

        # Change the view based on the selected item
        if item.text(column) == "Options":
            self.main_layout.addWidget(self.options_view)
            self.options_view.show()
        elif item.text(column) == "Overview":
            self.main_layout.addWidget(self.overview_view)
            self.overview_view.show()

        self.main_layout.setStretch(1, 1)
