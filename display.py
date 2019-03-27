# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import pandas as pd

class Ui_Display(object):

    def disp_close(self):
        Display.close()
           
    def setupUi(self, Display):
        Display.setObjectName("Display")
        Display.resize(753, 546)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("99129-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Display.setWindowIcon(icon)
        Display.setTabShape(QtWidgets.QTabWidget.Rounded)
        Display.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(Display)
        self.centralwidget.setObjectName("centralwidget")
        self.disp_table = QtWidgets.QTableWidget(self.centralwidget)
        self.disp_table.setGeometry(QtCore.QRect(70, 80, 621, 371))
        self.disp_table.setObjectName("disp_table")
        row=data.shape[0]
        col=data.shape[1]
        self.disp_table.setRowCount(row)
        self.disp_table.setColumnCount(col)
        for x in range(5):
            for y in range(5):
                self.disp_table.setItem(x, y, QTableWidgetItem(str(data.loc[x][y])))
        #self.disp_table.setHorizontalHeaderLabels()
        self.disp_label = QtWidgets.QLabel(self.centralwidget)
        self.disp_label.setGeometry(QtCore.QRect(206, 20, 341, 31))
        self.disp_label.setText("")
        self.disp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.disp_label.setObjectName("disp_label")
        self.disp_button = QtWidgets.QPushButton(self.centralwidget)
        self.disp_button.setGeometry(QtCore.QRect(494, 470, 161, 31))
        self.disp_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.disp_button.setObjectName("disp_button")
        self.disp_button.clicked.connect(self.disp_close)
        Display.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Display)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar.setObjectName("menubar")
        Display.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Display)
        self.statusbar.setObjectName("statusbar")
        Display.setStatusBar(self.statusbar)

        self.retranslateUi(Display)
        QtCore.QMetaObject.connectSlotsByName(Display)
        
        

    def retranslateUi(self, Display):
        _translate = QtCore.QCoreApplication.translate
        Display.setWindowTitle(_translate("Display", "Real Estate"))
        self.disp_button.setText(_translate("Display", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet('QMainWindow{background-color: white;border: 1px solid black;}')
    Display = QtWidgets.QMainWindow()
    ui = Ui_Display()
    data=pd.read_csv("data.csv")
    ui.setupUi(Display)
    Display.show()
    sys.exit(app.exec_())

