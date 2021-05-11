from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import filler
import connect_sql
#from connect_sql import Sql
from sign_up import Ui_Dialog as sign_up

#from user_window_controller import user_Window
import sign_in_controller

#from sign_in_controller import sign_inWindow
from artist_window_controller import artist_Window
from user_window_controller import user_Window



class sign_upWindow(QtWidgets.QMainWindow):
    def __init__(self) :
        super().__init__()
        self.ui = sign_up()
        self.ui.setupUi(self)
        self.setWindowTitle("Регистрация нового пользователя")

        self.db = connect_sql.Sql()

        self.ui.back_button.clicked.connect(self.back_button_clicked)
        self.ui.sign_up_button.clicked.connect(self.sign_up_button_clicked)

        # self.ui.passwodCheckbox. stateChanged.connect(self.checkboxHandler)
        #self.ui.sign_up_button.clicked.connect(self.createButton_clicked)

    def back_button_clicked(self):
        print("Bibop")


    def sign_up_button_clicked(self):
        name = str(self.ui.name_lineEdit.text())
        date_of_birth = self.ui.date_of_birth_dateEdit.date().toPyDate()
        country = str(self.ui.country_lineEdit.text())
        login = str(self.ui.login_lineEdit.text())
        password = str(self.ui.password_lineEdit.text())
        check_password = str(self.ui.check_password_lineEdit.text())
        email = str(self.ui.email_lineEdit.text())
        if self.ui.user_radio.isChecked():
            role_id =3
            self.db.cursor.execute("INSERT INTO users(role_id,password,login,email,date_of_bitth,country,name)" \
                                   "VALUES ( '"+str(role_id)+"','"+str(password)+"','"+str(login)+"','"+str(email)+"','"+str(date_of_birth)+"','"+str(country)+"','"+str(name)+"')")
            self.db.cnxn.commit()
            self.main = sign_in_controller.sign_inWindow()
            #self.main = user_Window()
            self.main.show()
            self.close()

        elif self.ui.artist_radio.isChecked():
            role_id=2
            self.db.cursor.execute("INSERT INTO users(role_id,password,login,email,date_of_bitth,country,name)" \
                                   "VALUES ( '" + str(role_id) + "','" + str(password) + "','" + str(login) + "','" + str(email) + "','" + str(date_of_birth) + "','" + str(country) + "','" + str(name) + "')")
            self.db.cnxn.commit()
            self.main=sign_in_controller.sign_inWindow()
            #self.main = artist_Window()
            self.main.show()
            self.close()

        elif not self.ui.user_radio.isChecked() and not self.ui.artist_radio.isChecked():
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Некорректный ввод")
            error_message.showMessage('Выберите вид аккаунта')




