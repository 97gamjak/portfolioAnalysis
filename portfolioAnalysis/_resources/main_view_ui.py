# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(401, 376)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.overview = QWidget()
        self.overview.setObjectName(u"overview")
        self.tabWidget.addTab(self.overview, "")
        self.positions = QWidget()
        self.positions.setObjectName(u"positions")
        self.tabWidget.addTab(self.positions, "")
        self.analytics = QWidget()
        self.analytics.setObjectName(u"analytics")
        self.tabWidget.addTab(self.analytics, "")

        self.vboxLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 401, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overview), QCoreApplication.translate("MainWindow", u"Overview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.positions), QCoreApplication.translate("MainWindow", u"Positions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analytics), QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        pass
    # retranslateUi

