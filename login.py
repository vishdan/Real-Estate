# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from check_login import check

class Ui_Login(object):
    def accept(self):
        username=self.user_line.text()
        password=self.pass_line.text()
        val=check(username,password)
        self.lab_err.setAlignment(QtCore.Qt.AlignCenter)
        if(val == 0):
            self.lab_err.setText("Invalid Username/Password")
            self.pass_line.setText("")
            self.user_line.setText("")
        else:
            self.lab_err.setText("Access Granted")


    def setupLogin(self, Login):
        Login.setObjectName("Login")
        Login.resize(431, 324)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("99129-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Login)
        self.buttonBox.setGeometry(QtCore.QRect(30, 270, 341, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(110, 30, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.user_line = QtWidgets.QLineEdit(Login)
        self.user_line.setGeometry(QtCore.QRect(210, 99, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_line.setFont(font)
        self.user_line.setObjectName("user_line")
        self.pass_line = QtWidgets.QLineEdit(Login)
        self.pass_line.setGeometry(QtCore.QRect(210, 169, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_line.setFont(font)
        self.pass_line.setFrame(True)
        self.pass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_line.setObjectName("pass_line")
        self.lab_err = QtWidgets.QLabel(Login)
        self.lab_err.setGeometry(QtCore.QRect(86, 220, 271, 31))
        self.lab_err.setText("")
        self.lab_err.setObjectName("lab_err")

        self.retranslateUi(Login)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Login.reject)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "LOGIN"))
        self.label_2.setText(_translate("Login", "User name:"))
        self.label_3.setText(_translate("Login", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupLogin(Login)
    Login.show()
    sys.exit(app.exec_())

