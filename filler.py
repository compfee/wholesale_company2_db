import datetime
from itertools import groupby

from PyQt5 import QtWidgets
from sign_in import Ui_Dialog as loginWindow
import user_info
from PyQt5.QtWidgets import QMessageBox



def fillComboBox(comboBox, cursor):
    #comboBox.clear()
    comboBox.addItem("")
    for i in cursor:
        comboBox.addItem(str(i[0]))

    #обработчик нажатия на кнопку - формирования таблицы
def fillTable(table, cursor, columnCount):

    table.setRowCount(0)
    i = 0
    row = cursor.fetchone()
    while (row is not None):
        item = QtWidgets.QTableWidgetItem()
        #item.sortItems(0, QtCore.Qt.AscendingOrder)
        table.setRowCount(table.rowCount() + 1)
        table.setVerticalHeaderItem(i, item)
        for j in range(columnCount):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
            # self.ui.med_card_tableWidget.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
        row = cursor.fetchone()
        i += 1

    table.resizeColumnsToContents()

def changeNummer(obj) :
    new_phone = obj.ui.phone_number_box.text()
    if new_phone.isdecimal() and len(new_phone) == 11:
        obj.db.cursor.execute("SELECT phone from  authentication_data  WHERE id= %s",
                               str(user_info.current_userID))
        old_phone = obj.db.cursor.fetchone()
        if old_phone[0] != new_phone:
            obj.db.cursor.execute("UPDATE authentication_data SET phone = %s WHERE id = %s",
                                   (new_phone, user_info.current_userID))
            obj.db.cnxn.commit()
            msg = QtWidgets.QMessageBox(obj)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Успех")
            msg.setText("Номер поменян успешно")
            msg.show()
    else:
        error_message = QtWidgets.QErrorMessage(obj)
        error_message.setWindowTitle("Ошибка входа")
        error_message.showMessage('Неправильный формат ввода номера. Попробуйте еще раз')
        obj.db.cursor.execute("SELECT phone from  authentication_data  WHERE id= %s",
                               str(user_info.current_userID))
        phone = obj.db.cursor.fetchone()

        obj.ui.phone_number_box.setText(str(phone[0]))


def exitButton(obj) :
    message = 'Вы уверены, что хотите выйти?'
    reply = QtWidgets.QMessageBox.question('Выход из базы данных', message,
                                           QtWidgets.QMessageBox.Yes,
                                           QtWidgets.QMessageBox.No)
    if reply == QtWidgets.QMessageBox.Yes:
        user_info.current_role = 0
        user_info.current_userID = 0
        obj.main = loginWindow()
        obj.main.show()
        obj.close()
    #обработчик работы со временем

def checkio(x):
    for _, j in groupby(x.split(), key=str.isalpha):
        if sum(1 for el in j) == 3:
            return True
    return False

def check_correctness(obj, name, date_of_birth, passport, phone, password, age) :
    if not (checkio(name)):
        error_message = QtWidgets.QErrorMessage(obj)
        error_message.setWindowTitle("Проверьте корректность ввода")
        error_message.showMessage('Введите ФИО')
        obj.ui.name_lineEdit.clear()
        return False

    elif (datetime.datetime.now().year - date_of_birth.year) < age:
        error_message = QtWidgets.QErrorMessage(obj)
        error_message.setWindowTitle("Проверьте корректность ввода")
        error_message.showMessage('Врач не может быть младше %s', age)
        obj.ui.date_of_birth_dateEdit.clear()
        return False

    elif len(passport) != 10:
        error_message = QtWidgets.QErrorMessage(obj)
        error_message.setWindowTitle("Проверьте корректность ввода")
        error_message.showMessage('Серия паспорта состоит из 10 цифр')
        obj.ui.passport_lineEdit.clear()
        return False

    elif not (phone.isdecimal()) and len(phone) != 11:
        error_message = QtWidgets.QErrorMessage(obj)
        error_message.setWindowTitle("Проверьте корректность ввода")
        error_message.showMessage('Проверьте корректность телефонного номера')
        obj.ui.phone_lineEdit.clear()
        return False


    elif len(password) < 4:
        error_message = QtWidgets.QErrorMessage(obj)
        error_message.setWindowTitle("Проверьте корректность ввода")
        error_message.showMessage('Пароль должен сожеражть больше символов')
        obj.ui.password_lineEdit.clear()
        return False

    return True

    #изменение номера телефона
def check_correctness_sign_up_data_for_patient(ui, name, date_of_birth, passport, phone, password, check_password, snils, insurance, contract_num) :

    if(check_password != password) :
        error_message = QtWidgets.QErrorMessage(ui)
        error_message.setWindowTitle("Проверьте корректность ввода")
        error_message.showMessage('Пароли не совпадают, попробуйте еще раз')

        ui.ui.password_lineEdit.clear()
        ui.ui.check_password_lineEdit.clear()
        return False

    if len(snils) != 9 and not(snils.isdecimal()) :
        error_message = QtWidgets.QErrorMessage(ui)
        error_message.setWindowTitle("Проверьте корректность ввода")
        error_message.showMessage('СНИЛС введен некореектно')

        ui.ui.snils_lineEdit.clear()
        return False

    if len(insurance) != 16 and not(insurance.isdecimal()) :
        error_message = QtWidgets.QErrorMessage(ui)
        error_message.setWindowTitle("Проверьте корректность ввода")
        error_message.showMessage('Номер страхового полиса введен некорректно')
        ui.ui.snils_lineEdit.clear()
        return False

    if len(contract_num) != 4 and not(contract_num.isdecimal()) :
        error_message = QtWidgets.QErrorMessage(ui)
        error_message.setWindowTitle("Проверьте корректность ввода")
        error_message.showMessage('Номер контракта - 5 цифр в контракте у вашей подписи')
        ui.ui.contract_num_lineEdit.clear()
        return False

    return check_correctness(ui, name, date_of_birth, passport, phone, password, 12)

def delete_row(obj, table, table_name, index_column):
    pasport = ""
    phone = ""
    for index in sorted(table.selectionModel().selectedRows()):
        row = index.row()
        index = table.model().index(row, index_column)
        passport = table.model().data(index)
        index = table.model().index(row, 2)
        phone = table.model().data(index)
        table.model().removeRow(row)
    if len(passport) > 0 and len(phone) > 0:
        if table_name == "Physicians" :
            obj.db.cursor.execute("DELETE FROM Physicians WHERE passport = '" + passport + "'")
        elif table_name == "Patients" :
            obj.db.cursor.execute("DELETE FROM Patients WHERE passport = '" + passport + "'")

        obj.db.cnxn.commit()
        print("Bibop")
        obj.db.cursor.execute("DELETE FROM authentication_data "
                               "WHERE phone = '" + phone + "'")
        obj.db.cnxn.commit()