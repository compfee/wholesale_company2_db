
import psycopg2
#from cryptography.fernet import Fernet

import user_info


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
        #cipher = Fernet(user_info.cipher_key)
        self.cursor.execute("select password,users.name from users where users.name = '" + login + "'")
        temp =self.cursor.fetchone()

        self.cursor.execute("select password, users.name from users where password='"+str(temp[0])+"' and users.name='"+str(temp[1])+"'")
        role_table=str(self.cursor.fetchone())
        if role_table==None:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle('Повторите ввод')
            error_message.showMessage('Данные неверны')

            return False, 0, 0
        else:
            self.cursor.execute("SELECT id from users WHERE password='"+str(temp[0])+"' and users.name='"+str(temp[1])+"'")
            temp1=self.cursor.fetchone()
            if temp[1].replace(' ', '') == password:
                 return True, temp[0], temp1[0]
            else:
                 return False, temp[0], temp1[0]
