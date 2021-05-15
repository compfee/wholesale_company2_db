
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import filler
import connect_sql
import psycopg2
import user_info
import sign_in_controller
from artist_window import Ui_Dialog as artist_window
import datetime


now = datetime.datetime.now()

class artist_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = artist_window()
        self.ui.setupUi(self)
        self.setWindowTitle("Исполнитель")

        self.db = connect_sql.Sql()
        self.db.cursor.execute(
            "SELECT id from users_wholesale where id = " + str(user_info.current_userID))
        global user_id
        user_id = self.db.cursor.fetchone()

        self.setInitialValues()

        self.ui.change_password_button_2.clicked.connect(self.change_password_clicked)
        self.ui.change_login_button.clicked.connect(self.change_login_clicked)

       # self.ui.change_nummer_button.clicked.connect(self.change_nummer_button_clicked)
        self.ui.exit_button.clicked.connect(self.exit_button_clicked)

        self.show()


    def exit_button_clicked(self):
        self.main = sign_in_controller.sign_inWindow()
        self.main.show()
        self.close()


    def setInitialValues(self):

        self.db.cursor.execute("SELECT login from users_wholesale  WHERE id= '"+str(user_info.current_userID)+"'")
        login = self.db.cursor.fetchone()
        self.ui.login_lineEdit.setText(str(login[0]))

        self.db.cursor.execute("SELECT password from users_wholesale  WHERE id= '"+str(user_info.current_userID)+"'")
        password = self.db.cursor.fetchone()
        self.ui.password_lineEdit.setText(str(password[0]))

        self.db.cursor.execute(
            "select goods.id,name,w.good_count as warehouse1,w22.good_count as warehouse2 from goods left join warehouse1 w on goods.id = w.good_id left join warehouse2 w22 on goods.id = w22.good_id ")
        filler.fillTable(self.ui.user_goods_catalogue_tableWIdget, self.db.cursor, 4)

       # self.songs_change()


    def change_password_clicked(self):
        new_pass=str(self.ui.password_lineEdit.text())
        new_pass2=str(self.ui.password_confirm_lineEdit.text())
        if not new_pass==new_pass2:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle('Повторите ввод')
            error_message.showMessage('Пароли не совпадают')
        else:
            try:
                self.db.cursor.execute(
                    "update users set password='" + new_pass + "' where user_id='" + str(user_info.current_userID) + "'")
                self.db.cnxn.commit()
                self.db.cursor.execute("SELECT password from users  WHERE user_id= '"+str(user_info.current_userID)+"'")
                password = self.db.cursor.fetchone()
                self.ui.password_lineEdit.setText(str(password[0]))
                print("smth happened")
            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)

    def change_login_clicked(self):
        new_login=str(self.ui.login_lineEdit.text())
        all_logins=self.db.cursor.execute("select name from users where name='"+new_login+"'")

        if not (new_login.isalnum()) and len(new_login) < 3 or all_logins!=None:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Некорректный ввод")
            error_message.showMessage('Введите другой логин')

        else:
            try:
                self.db.cursor.execute("update users set login='"+new_login+"' where user_id='"+str(user_info.current_userID)+"'")
                self.db.cnxn.commit()
                self.db.cursor.execute("SELECT login from users  WHERE user_id= '"+str(user_info.current_userID)+"'")
                login = self.db.cursor.fetchone()
                self.ui.login_lineEdit.setText(str(login[0]))
                print("smth happened")
            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)


    def add_button_clicked(self):
        new_name = str(self.ui.good_name_lineEdit.text())
        if not (new_name.isalnum()) and len(new_name) < 3:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Некорректный ввод")
            error_message.showMessage('Введите другое наименование')
        else:
            good_name = new_name
            w1 = str(self.ui.w1_lineEdit.text())
            w2 = str(self.ui.w2_lineEdit.text())
            priority = str(self.ui.priority_lineEdit.text())
            id = str(self.ui.id_lineEdit.text())
            try:
                self.db.cursor.execute(
                    "insert into goods(name,priority,id) values  %s, %s, %s)",
                     (good_name, priority,id))
                # datetime.datetime.today().strftime('%Y-%m-%d')
                self.db.cursor.execute(
                    "insert into warehouse1( good_id, good_count) values %s, %s)",
                    (id, w1))
                self.db.cursor.execute(
                    "insert into warehouse2( good_id, good_count) values %s, %s)",
                    (id, w2))
                self.db.cnxn.commit()
                self.artist_songs_change()

                print("smth happened")
            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)
