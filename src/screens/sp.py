import logging
import random
import sys
import time

from PyQt5.QtCore import QRunnable, Qt, QThreadPool
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(674, 450)
        SplashScreen.setStyleSheet("background-color: white;")
        self.verticalLayout = QtWidgets.QVBoxLayout(SplashScreen)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.gridLayout.setObjectName("gridLayout")
        self.Title_2 = QtWidgets.QLabel(SplashScreen)
        self.Title_2.setStyleSheet("font: 87 32pt \"Gilroy\";\n"
                                   "font-weight: 900;\n"
                                   "color: black;")
        self.Title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_2.setWordWrap(True)
        self.Title_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Title_2.setObjectName("Title_2")
        self.gridLayout.addWidget(self.Title_2, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(SplashScreen)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 40))
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: #AFFFEC;\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: #00E5AE;\n"
                                       "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "Form"))
        self.Title_2.setText(_translate("SplashScreen", "ARTIFICIAL INTELLIGENCE IN NEW NORMAL LEARNING"))


app = QApplication(sys.argv)
window = Ui_SplashScreen()
window.show()
sys.exit(app.exec())
