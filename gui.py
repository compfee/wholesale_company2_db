# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 187)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 20, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro ExtraLight")
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 140, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Welcome to our music service!"))
        self.pushButton.setText(_translate("Dialog", "Let me in"))
        self.pushButton_2.setText(_translate("Dialog", "I\'m new here"))
