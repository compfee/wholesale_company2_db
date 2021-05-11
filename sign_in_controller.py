from PyQt5 import QtWidgets
import filler
import user_info
from sign_in import Ui_Dialog as loginmain
from user_window_controller import user_Window
from sign_up_controller import sign_upWindow
from artist_window_controller import artist_Window
import connect_sql

class sign_inWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loginmain()
        self.ui.setupUi(self)
        self.setWindowTitle("Вход")

        self.ui.sign_in_button.clicked.connect(self.sign_in_button_clicked)
        self.ui.sign_up_button.clicked.connect(self.sign_up_button_clicked)

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
            status,password, id = self.db.checkPassword(l, p)
            if (status == False):
                message = "Не найден пользователь с таким логином/паролем"
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка входа")
                error_message.showMessage(message)
                self.ui.password_lineEdit.clear()
            else:
                # user_info.current_role = p
                user_info.current_userID = id

                print('user')
                self.menu = user_Window()

                self.close()
                self.menu.show()

    def sign_up_button_clicked(self):
        self.db.cursor.execute("delete from users_orders")
        self.db.cursor.execute(
            "select song_name,artist_name,ganre,price,upload_date from users_orders where current_user_id='" + str(
                user_info.current_userID) + "'")
        filler.fillTable(self.ui.basket_tableWidget, self.db.cursor, 5)
        self.ui.count_label.setText(str(0))
        self.main = sign_upWindow()
        #self.main = user_Window()
        self.main.show()
        self.close()