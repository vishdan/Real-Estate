# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from login import *
from check_login import *

class Ui_First(object):
    def login(self):
        self.log = QtWidgets.QDialog()
        self.ui=Ui_Login()
        self.ui.setupLogin(self.log)
        self.log.show()

    def setupUi(self, First):
        First.setObjectName("First")
        First.resize(740, 426)
        First.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("99129-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        First.setWindowIcon(icon)
        First.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(First)
        self.centralwidget.setObjectName("centralwidget")
        self.Admin_log_but = QtWidgets.QPushButton(self.centralwidget)
        self.Admin_log_but.setGeometry(QtCore.QRect(570, 320, 91, 31))
        self.Admin_log_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Admin_log_but.setObjectName("Admin_log_but")
        self.Admin_log_but.clicked.connect(self.login)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 150, 571, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Invest_But = QtWidgets.QPushButton(self.frame)
        self.Invest_But.setGeometry(QtCore.QRect(40, 40, 121, 51))
        self.Invest_But.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Invest_But.setObjectName("Invest_But")
        self.Buy_but = QtWidgets.QPushButton(self.frame)
        self.Buy_but.setGeometry(QtCore.QRect(380, 40, 121, 51))
        self.Buy_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Buy_but.setObjectName("Buy_but")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(176, 42, 371, 41))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        First.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(First)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 21))
        self.menubar.setObjectName("menubar")
        First.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(First)
        self.statusbar.setObjectName("statusbar")
        First.setStatusBar(self.statusbar)

        self.retranslateUi(First)
        QtCore.QMetaObject.connectSlotsByName(First)

    def retranslateUi(self, First):
        _translate = QtCore.QCoreApplication.translate
        First.setWindowTitle(_translate("First", "Real Estate"))
        self.Admin_log_but.setText(_translate("First", "ADMIN LOGIN"))
        self.Invest_But.setText(_translate("First", "Invest/Properties"))
        self.Buy_but.setText(_translate("First", "Buy/Homes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet('QMainWindow{background-color: white;border: 1px solid black;}')
    First = QtWidgets.QMainWindow()
    ui = Ui_First()
    ui.setupUi(First)
    First.show()
    sys.exit(app.exec_())

