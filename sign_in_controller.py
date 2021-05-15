from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit
import filler
import user_info
from sign_in import Ui_Dialog as loginmain
from user_window_controller import user_Window

from artist_window_controller import artist_Window
import connect_sql

class sign_inWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loginmain()
        self.ui.setupUi(self)
        self.setWindowTitle("Вход")

        self.ui.sign_in_button.clicked.connect(self.sign_in_button_clicked)

        self.ui.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.db = connect_sql.Sql()

    def sign_in_button_clicked(self):
        l = self.ui.phone_lineEdit.text()
        p = self.ui.password_lineEdit.text()
        if (l.strip() == ''):
            message = "Введите логин"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            if len(l) != 0:
                self.ui.phone_lineEdit.clear()
            self.ui.password_lineEdit.clear()
        elif (p.strip() == ''):
            message = "Пароль не введен. Попробуйте еще раз!"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            if len(p) != 0:
                self.ui.password_lineEdit.clear()

        elif (p.find(' ') != -1):
            message = "Данного пользователя не существует или введен неверный пароль! Проверьте правильность данных и повторите вход."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            self.ui.password_lineEdit.clear()

        else: # если прошли все проверки начинаем проверку пользователя по БД
            status, role, id = self.db.checkPassword(l, p)
            if (status == False):
                message = "Не найден пользователь с таким логином/паролем"
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка входа")
                error_message.showMessage(message)
                self.ui.password_lineEdit.clear()
            else:
                user_info.current_role = role
                user_info.current_userID = id
                if user_info.current_role == 0:
                    print('user')
                    self.menu = user_Window()
                elif user_info.current_role == 1:
                    self.db.cursor.execute("SELECT role_id from users_wholesale where id = '"+str(id)+"'")
                    role_id = self.db.cursor.fetchone()
                    self.menu = artist_Window()
                    print('artist')

                self.close()
                self.menu.show()

