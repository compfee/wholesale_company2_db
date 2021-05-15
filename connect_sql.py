
import psycopg2
from cryptography.fernet import Fernet

import user_info
from PyQt5 import QtWidgets

class Sql:
    def __init__(self):  # конструктор, self = this, если используется нужно обьявлять, неявно не задано
        try:
            self.cnxn = psycopg2.connect(user="postgres",
                                         password="root",
                                         host="localhost",
                                         port="5432",
                                         database="wholesale_company",
                                         options="-c search_path=dbo,public")
            self.cursor = self.cnxn.cursor()

            print(self.cnxn.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def checkPassword(self, login, password):
        cipher = Fernet(user_info.cipher_key)
        self.cursor.execute("SELECT role_id, password,login from users_wholesale WHERE login = '" + login + "'")
        temp =self.cursor.fetchone()

        self.cursor.execute("select id, password,role_id  from users_wholesale where role_id='"+str(temp[0])+"' and password='"+str(temp[1])+"' and login='"+str(temp[2])+"'")
        role_table=self.cursor.fetchone()
        if role_table==None:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle('Повторите ввод')
            error_message.showMessage('Данные неверны')

            return False, 0, 0
        else:
            passw = cipher.decrypt(str.encode(role_table[1])).decode('utf8')
            self.cursor.execute("SELECT id from users_wholesale WHERE role_id='"+str(temp[0])+"' and password='"+str(temp[1])+"' and login='"+str(temp[2])+"'")
            temp1=self.cursor.fetchone()
            if password==passw:
                 return True, temp[0], temp1[0]
            else:
                 return False, temp[0], temp1[0]