import sys
import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sign_in_controller import sign_inWindow

from user_window_controller import user_Window
from artist_window_controller import artist_Window
from connect_sql import Sql
#from admin_controller import Admin_Controller
if __name__ == '__main__':

    db = Sql()

    app = QtWidgets.QApplication([])

    #window = Admin_Controller()
    #window = sign_upWindow()
    window = sign_inWindow()

    #window = user_Window()
    # window = artist_Window()
    window.show()

    db.cnxn.close()

    sys.exit(app.exec())

       # db.cnxn.close()
       # print("Error while connecting to PostgreSQL", error)
       # sys.exit(app.exec())
