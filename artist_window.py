# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'artist_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(885, 719)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 861, 696))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 811, 621))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.password_confirm_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password_confirm_lineEdit.setObjectName("password_confirm_lineEdit")
        self.gridLayout.addWidget(self.password_confirm_lineEdit, 2, 1, 1, 1)
        self.login_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.gridLayout.addWidget(self.login_lineEdit, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.change_password_button_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.change_password_button_2.setObjectName("change_password_button_2")
        self.gridLayout.addWidget(self.change_password_button_2, 2, 2, 1, 1)
        self.change_login_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.change_login_button.setObjectName("change_login_button")
        self.gridLayout.addWidget(self.change_login_button, 0, 2, 1, 1)
        self.password_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout.addWidget(self.password_lineEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.exit_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_3.addWidget(self.exit_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 861, 711))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.user_goods_catalogue_tableWIdget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.user_goods_catalogue_tableWIdget.setObjectName("user_goods_catalogue_tableWIdget")
        self.user_goods_catalogue_tableWIdget.setColumnCount(5)
        self.user_goods_catalogue_tableWIdget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.user_goods_catalogue_tableWIdget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_goods_catalogue_tableWIdget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_goods_catalogue_tableWIdget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_goods_catalogue_tableWIdget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_goods_catalogue_tableWIdget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_3.addWidget(self.user_goods_catalogue_tableWIdget)
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Личный кабинет пользователя"))
        self.label_11.setText(_translate("Dialog", "Повторите пароль"))
        self.label_8.setText(_translate("Dialog", "Логин"))
        self.label_9.setText(_translate("Dialog", "Пароль"))
        self.change_password_button_2.setText(_translate("Dialog", "Изменить пароль"))
        self.change_login_button.setText(_translate("Dialog", "Изменить логин"))
        self.exit_button.setText(_translate("Dialog", "Выйти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Личный кабинет"))
        item = self.user_goods_catalogue_tableWIdget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "id"))
        item = self.user_goods_catalogue_tableWIdget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Наименование"))
        item = self.user_goods_catalogue_tableWIdget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Склад1"))
        item = self.user_goods_catalogue_tableWIdget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Склад2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Список товаров"))
