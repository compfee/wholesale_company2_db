import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import filler
import connect_sql
from user_info import current_userID as doc_id
from user_window import Ui_MainWindow as User_window
import user_info
import datetime

now = datetime.datetime.now()

import sign_in_controller

class user_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = User_window()
        self.ui.setupUi(self)
        self.setWindowTitle("Пользователь")

        self.db = connect_sql.Sql()
        self.show_all_goods()
        self.ui.add_button.clicked.connect(self.add_button_clicked)
        self.goods_list_change()
        self.sales_list_change()
        self.ui.count1_button.clicked.connect(self.count1)
        self.setInitialValues()
        self.ui.delete_button.clicked.connect(self.delete_good)
        # self.ui.change_button.clicked.connect(self.change_button_clicked)
        self.ui.sort_button_name_prior.clicked.connect(self.sort_button_name_prior_clicked)
        # self.ui.sort_button_prior.clicked.connect(self.sort_button_prior_clicked)
        self.ui.under_prior_button.clicked.connect(self.under_prior_button_clicked)
        self.ui.not_on_w1_button.clicked.connect(self.not_on_w1_button_clicked)
        self.ui.all_sales_button.clicked.connect(self.all_sales_button_clicked)
        self.ui.sales_not_on_date_button.clicked.connect(self.sales_not_on_date_button_clicked)
        self.ui.sum_w1_w2_button.clicked.connect(self.sum_w1_w2_button_clicked)
        self.ui.add_sale_button.clicked.connect(self.add_sale_button_clicked)
        self.ui.top5_button.clicked.connect(self.top5_button_clicked)
        self.ui.delete_sales_under_date.clicked.connect(self.delete_sales_under_date_clicked)
        self.ui.delete_goods_without_sales.clicked.connect(self.delete_goods_without_sales_clicked)
        self.ui.delete_good_and_its_sales.clicked.connect(self.delete_good_and_its_sales_clicked)
        self.ui.delete_good_with_min_prior.clicked.connect(self.delete_good_with_min_prior_clicked)
        self.ui.change_button.clicked.connect(self.change_button_clicked)
        self.ui.delete_5_goods_button.clicked.connect(self.delete_5_goods_button_clicked)
        self.ui.delete_sale_button_2.clicked.connect(self.delete_sale_button_2_clicked)

        self.ui.change_button_2.clicked.connect(self.change_button_2_clicked)

        # self.ui.change_button_3.clicked.connect(self.change_button_3_clicked)

        self.ui.create_view_button.clicked.connect(self.create_view_button_clicked)
        self.ui.create_view_button_2.clicked.connect(self.create_view_button_2_clicked)

        self.ui.create_xp1_button.clicked.connect(self.create_xp1_button_clicked)
        self.ui.create_xp2_button.clicked.connect(self.create_xp2_button_clicked)
        self.ui.create_xp3_button.clicked.connect(self.create_xp3_button_clicked)
        self.ui.create_xp4_button.clicked.connect(self.create_xp4_button_clicked)
        self.ui.create_xp5_button.clicked.connect(self.create_xp5_button_clicked)

        self.ui.sales_catalogue_tableWidget.setSortingEnabled(True)
        self.ui.catalogue_tableWidget_2.setSortingEnabled(True)
        self.show()


    def delete_sale_button_2_clicked(self):
      try:
        row = self.ui.sales_catalogue_tableWidget.currentRow()
        column = self.ui.sales_catalogue_tableWidget.currentColumn()
        id = str(self.ui.sales_catalogue_tableWidget.item(row, 0).text())
        # id=str(self.ui.lineEdit_sale_id_delete.text())
        self.db.cursor.execute("delete from sales where good_id='" + id + "'")
        self.db.cnxn.commit()
        self.sales_list_change()
      except (Exception, psycopg2.Error) as error:
        self.db.cursor.execute("rollback")
        self.db.cnxn.commit()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('{}'.format(error))
        msg.setInformativeText('У этого товара есть приоритет')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

#Создать хранимую процедуру с входными параметрами, задающими
#интервал времени, и выходным параметром – товар, с минимальным числом
#продаж за заданный период времени.
    def create_xp5_button_clicked(self):

        date1 = self.ui.dateEdit_count1_3.text()
        date2 = self.ui.dateEdit_count1_4.text()
        self.db.cursor.execute(
            "select * from min_demand('" + str(date1) + "','" + str(date2) + "');" )
        self.db.cnxn.commit()
        filler.fillTable(self.ui.dates_tableWidget_2, self.db.cursor, 1)





#1 Создать хранимую процедуру с входными параметрами, задающими
#интервал времени, и выходным – идентификатором товара. Процедура
#должна возвращать товар с максимальным приростом спроса

    def create_xp4_button_clicked(self):

        date1 = self.ui.dateEdit_count1_3.text()
        date2 = self.ui.dateEdit_count1_4.text()
        self.db.cursor.execute(
            "select * from max_demand('" + str(date1) + "','" + str(date2) + "');" )
        self.db.cnxn.commit()
        filler.fillTable(self.ui.dates_tableWidget_2, self.db.cursor, 1)


#2 Создать хранимую процедуру, имеющую два параметра «товар1» и
#«товар2». Она должна возвращать даты, спрос в которые на «товар1» был
#больше чем на «товар2». Если в какой-либо день один из товаров не
#продавался, такой день не рассматривается

    def create_xp3_button_clicked(self):
        id1 = str(self.ui.id1_lineEdit.text())
        id2 = str(self.ui.id2_lineEdit.text())
        self.db.cursor.execute("select * from demand('" + id1 + "','" + id2 + "')")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.dates_tableWidget, self.db.cursor, 1)


#1 Создать хранимую процедуру с параметром количество перевозимого
#товара за ближайший рейс и выводящую все товары, которые необходимо
#привезти, и их количество
    def create_xp2_button_clicked(self):
        count = str(self.ui.delivery_lineEdit.text())
        self.db.cursor.execute("select * from delivery_from_2_to_1();select * from delivery_from_2_to_1_with_quant(%s)", [count])
        self.db.cnxn.commit()
        filler.fillTable(self.ui.catalogue_tableWidget_2, self.db.cursor, 6)



#1 Создать хранимую процедуру, выводящую список товаров для перевоза и
#его количество согласно текущему состоянию приоритетов

    def create_xp1_button_clicked(self):
        self.db.cursor.execute("select * from delivery_from_2_to_1()")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.catalogue_tableWidget_2, self.db.cursor, 6)

#2 Создать представление, отображающее 5 самых популярных товаров за заданный
#месяц

    def create_view_button_2_clicked(self):
        date = str(self.ui.dateEdit_view.text())
        date1=date.split('.')
        date2=str(date1[2]+'-'+date1[1]+'-%');
        self.db.cursor.execute(
            "select goods.id,name,w.good_count as warehouse1,w22.good_count as warehouse2,count(s.good_id ) as count from goods left join warehouse1 w on goods.id = w.good_id left join warehouse2 w22 on goods.id = w22.good_id join sales s on goods.id = s.good_id where create_date::text like '" + date2 + "' group by goods.id, name , warehouse1,warehouse2 order by count desc limit 5;")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.catalogue_tableWidget_2, self.db.cursor, 5)

    #1 Создать представление, отображающее все товары, число которых на складе1
#менее некоторого числа
    def create_view_button_clicked(self):
        count = self.ui.view_lineEdit.text()
        self.db.cursor.execute("select goods.id,name,w.good_count as warehouse1,w22.good_count as warehouse2,priority from goods left join warehouse1 w on goods.id = w.good_id left join warehouse2 w22 on goods.id = w22.good_id where w.good_count<'" + count + "'")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.catalogue_tableWidget_2, self.db.cursor, 5)



#модификация в рамках транзакции
#1 В рамках транзакции поменять заданный товар во всех заявках на другой и
#удалить его.
    # def change_button_2_clicked(self):
    #     id1 = int(str(self.ui.lineEdit_id_change.text()))
    #     id2 = int(str(self.ui.lineEdit_id_change2.text()))
    #     self.db.cursor.execute("call replace_good(%s,%s)",(id1,id2))
    #     self.db.cnxn.commit()
    #     self.goods_list_change()
    #     self.sales_list_change()
#2 то же, что и п1, но транзакцию откатить
    def change_button_2_clicked(self):
      try:
        id1 = int(str(self.ui.lineEdit_id_change.text()))
        id2 = int(str(self.ui.lineEdit_id_change2.text()))
        self.db.cursor.execute("call replace_good(%s,%s)",(id1,id2))
        self.db.cnxn.commit()
        self.goods_list_change()
        self.sales_list_change()
      except (Exception, psycopg2.Error) as error:
        self.db.cursor.execute("rollback")
        self.db.cnxn.commit()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('{}'.format(error))
        msg.setInformativeText('Невозможно заменить id на несуществующий')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

#Списать 5 единиц заданного товара со «склада 1». Если количество товара
#на этом складе меньше 5, не достающее число списать со второго склада

    def delete_5_goods_button_2_clicked(self):
        id = int(str(self.ui.delete_5_goods_lineEdit_2.text()))
        self.db.cursor.execute("call proc2(%s)", ([id]))
        self.db.cnxn.commit()
        self.goods_list_change()

#Списать 5 единиц заданного товара со «склада 1»
    def delete_5_goods_button_clicked(self):

        id=str(self.ui.delete_5_goods_lineEdit.text())
        self.db.cursor.execute(
            "select good_count from warehouse1 where good_id='" + id + "' ")
        count=self.db.cursor.fetchone()
        if count[0]>5:
            self.db.cursor.execute(
            "update warehouse1 set good_count=good_count-5 where good_id='" + id + "' ")
        else:
            self.db.cursor.execute("call proc2(%s)", ([id]))
        self.db.cnxn.commit()
        self.goods_list_change()


#1 Изменить количество товаров с заданным наименованием
    def change_button_clicked(self):
        row = self.ui.catalogue_tableWidget_2.currentRow()
        column = self.ui.catalogue_tableWidget_2.currentColumn()
        id = self.ui.catalogue_tableWidget_2.item(row, 0).text()
        text = self.ui.catalogue_tableWidget_2.item(row, column).text()

        if column==0:
          try:
            good_id = str(self.ui.id_lineEdit.text())

            if good_id!='':
             self.db.cursor.execute(
                "update goods set id='" + good_id + "'where id='" + id + "' ")

             self.db.cnxn.commit()
             self.goods_list_change()

          except (Exception, psycopg2.Error) as error:
              self.db.cursor.execute("rollback")
              self.db.cnxn.commit()
              msg = QMessageBox()
              msg.setIcon(QMessageBox.Critical)
              msg.setText('{}'.format(error))
              msg.setInformativeText('Существуют связи, невозможно изменить id или поле пустое')
              msg.setWindowTitle("Ошибка")
              msg.exec_()
        elif column==1:
            good_name = str(self.ui.good_name_lineEdit.text())
            try:
                self.db.cursor.execute(
                "update goods set name='" + good_name + "'where id='" + id + "' ")
                self.db.cnxn.commit()
                self.goods_list_change()
            except (Exception, psycopg2.Error) as error:
                self.db.cursor.execute("rollback")
                self.db.cnxn.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('{}'.format(error))
                msg.setInformativeText('')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
        elif column==2:

            w1 = str(self.ui.w1_lineEdit.text())
            try:
              if text=="None":

                self.db.cursor.execute(
                    "insert into warehouse1(good_id, good_count) values ('" + id + "','" + w1 + "')")
              else:
                 self.db.cursor.execute(
                "update warehouse1 set good_count='" + w1 + "'where id='" + id + "' ")
              self.db.cnxn.commit()
              self.goods_list_change()
            except (Exception, psycopg2.Error) as error:
                self.db.cursor.execute("rollback")
                self.db.cnxn.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('{}'.format(error))
                msg.setInformativeText('')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
        elif column==3:
            w2 = str(self.ui.w1_lineEdit.text())
            try:
             if text == "None":
                self.db.cursor.execute(
                    "insert into warehouse2(good_id, good_count) values ('" + id + "','" + w2 + "')")
             else:
                self.db.cursor.execute(
                    "update warehouse2 set good_count='" + w2 + "'where id='" + id + "' ")
             self.db.cnxn.commit()
             self.goods_list_change()
            except (Exception, psycopg2.Error) as error:
                self.db.cursor.execute("rollback")
                self.db.cnxn.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('{}'.format(error))
                msg.setInformativeText('')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
        elif column==4:
            priority = str(self.ui.priority_lineEdit.text())
            try:
             self.db.cursor.execute(
                "update goods set priority='" + priority + "'where id='" + id + "' ")
             self.db.cnxn.commit()
             self.goods_list_change()
            except (Exception, psycopg2.Error) as error:
                self.db.cursor.execute("rollback")
                self.db.cnxn.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('{}'.format(error))
                msg.setInformativeText('')
                msg.setWindowTitle("Ошибка")
                msg.exec_()



    #2 то же, что и п1, но транзакцию откатить

#1 Удалить в рамках транзакции товар со «склада 1» с наименьшим приоритетом
    def delete_good_with_min_prior_clicked(self):
        self.db.cursor.execute("call proc1()")
        self.db.cnxn.commit()
        self.goods_list_change()

# 3 Удалить товар и заявки на него
    def delete_good_and_its_sales_clicked(self):
        print("Bibop")
        row = self.ui.catalogue_tableWidget_2.currentRow()
        column = self.ui.catalogue_tableWidget_2.currentColumn()
        id = self.ui.catalogue_tableWidget_2.item(row, column).text()

        try:
            self.db.cursor.execute(
                "delete from sales where good_id='" + id + "'; delete from goods where id='" + id + "' ")
            self.db.cnxn.commit()
            self.goods_list_change()
            self.sales_list_change()

        except (Exception, psycopg2.Error) as error:
            self.db.cursor.execute("rollback")
            self.db.cnxn.commit()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('{}'.format(error))
            msg.setInformativeText('На этот товар установлен приоритет')
            msg.setWindowTitle("Ошибка")
            msg.exec_()

#2 Удалить товары, не имеющие заявок
    def delete_goods_without_sales_clicked(self):
        self.db.cursor.execute(
            "delete from goods where id not in (select good_id from sales) and priority=0")
        self.db.cnxn.commit()
        self.goods_list_change()

#1 Удалить заявки, у которых дата меньше заданной
    def delete_sales_under_date_clicked(self):
        date1 = str(self.ui.dateEdit_count1.text())

        self.db.cursor.execute(
                "delete from sales where good_id in (select id from goods where priority=0) and create_date<'"+str(date1)+"'")
        self.db.cnxn.commit()
        self.sales_list_change()

#2 Добавить заявку на товар из п1
    def add_sale_button_clicked(self):
       try:
        id = self.ui.lineEdit_id.text()
        count = self.ui.lineEdit_count.text()
        self.db.cursor.execute("insert into sales(good_id,create_date,good_count) values (%s,%s,%s)",
                               (id, datetime.datetime.today().strftime('%Y-%m-%d'), count))
        self.db.cnxn.commit()
        self.sales_list_change()
       except (Exception, psycopg2.Error) as error:
           self.db.cursor.execute("rollback")
           self.db.cnxn.commit()
           msg = QMessageBox()
           msg.setIcon(QMessageBox.Critical)
           msg.setText('{}'.format(error))
           msg.setInformativeText('Недостаточно единиц товара на складах или число товара меньше 1')
           msg.setWindowTitle("Ошибка")
           msg.exec_()

#2 Пять самых популярных товаров за заданный промежуток времени, упорядочив в порядке уменьшения спроса
    def top5_button_clicked(self):

        date1 = self.ui.dateEdit_count1_3.text()
        date2 = self.ui.dateEdit_count1_4.text()
        self.db.cursor.execute(
            "select goods.id,name,w.good_count as warehouse1,w22.good_count as warehouse2,count(s.good_id ) as count from goods left join warehouse1 w on goods.id = w.good_id left join warehouse2 w22 on goods.id = w22.good_id join sales s on goods.id = s.good_id where create_date>='" + str(date1) + "' and create_date<='" + str(date2) + "' group by goods.id,name,warehouse1,warehouse2 order by count desc limit 5;")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.catalogue_tableWidget_2, self.db.cursor, 5)

    #1 Вывести суммарное количество заданного товара на первом и втором складах.
    def sum_w1_w2_button_clicked(self):
        good = self.ui.lineEdit_sum_w1_w2.text()
        self.db.cursor.execute(
            "select sum(good_count) from (select sum(good_count),good_id, good_count from warehouse1 where good_id='" + str(good) + "' group by good_id, good_count union select sum(good_count),good_id, good_count  from warehouse2 where good_id='" + str(good) + "' group by good_id, good_count ) as count")
        sum = self.db.cursor.fetchone()
        self.ui.label_count1.setText(str(sum[0]))


#2 Вывести количество товаров, на которые не было заявок за заданную дату
    def sales_not_on_date_button_clicked(self):
        date1 = self.ui.dateEdit_count1.text()
        self.db.cursor.execute(
            "select sum(good_count) from goods left join sales s on goods.id = s.good_id where create_date!='" + str(date1) + "'")
        count1 = self.db.cursor.fetchone()
        self.ui.label_count1.setText(str(count1[0]))

    #1 Вывести заявки и наименования товаров, включая товары, на которые не было заявок
    def all_sales_button_clicked(self):
        self.db.cursor.execute(
            "select s.id,goods.name,good_id,good_count,priority,create_date from goods left join sales s on goods.id = s.good_id;")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.sales_catalogue_tableWidget, self.db.cursor, 6)

#2 Вывести наименования на товары, отсутствующие на «складе 1»
    def not_on_w1_button_clicked(self):
        self.db.cursor.execute(
            "select goods.id,name,w.good_count as warehouse1,w22.good_count as warehouse2,priority from goods left join warehouse1 w on goods.id = w.good_id left join warehouse2 w22 on goods.id = w22.good_id where not exists( select * from warehouse1 where good_id=goods.id)")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.catalogue_tableWidget_2, self.db.cursor, 5)

#1 Вывести все заявки на товары с приоритетом меньше заданного
    def under_prior_button_clicked(self):
        prior1 = self.ui.lineEdit_prior.text()
        self.db.cursor.execute(
            "select sales.id,g.name,good_id,good_count,priority,create_date from sales join goods g on g.id = sales.good_id where priority<'" + str(prior1) + "'")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.sales_catalogue_tableWidget, self.db.cursor, 6)

#2 Посчитать количество товаров в заявках за заданную дату
    def count1(self):
        date1=self.ui.dateEdit_count1.text()

        self.db.cursor.execute(
            "select count(good_id) from sales where create_date='"+str(date1)+"'")
        count1=self.db.cursor.fetchone()

        self.ui.label_count1.setText(str(count1[0]))

#1 Вывести товары, упорядочив в алфавитном порядке по наименованию и в обратном порядке по приоритету
    def sort_button_name_prior_clicked(self):
        self.db.cursor.execute(
            "select goods.id,name,w.good_count as warehouse1,w22.good_count as warehouse2,priority from goods left join warehouse1 w on goods.id = w.good_id left join warehouse2 w22 on goods.id = w22.good_id  order by name asc , priority desc;")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.catalogue_tableWidget_2, self.db.cursor, 5)

    def sales_list_change(self):
        self.db.cursor.execute(
            "select sales.id,g.name,good_id,good_count,priority,create_date from sales join goods g on g.id = sales.good_id ")
        self.db.cnxn.commit()
        filler.fillTable(self.ui.sales_catalogue_tableWidget, self.db.cursor, 6)

    def setInitialValues(self):
        self.db.cursor.execute("SELECT users.name from users where id=" + str(user_info.current_userID))
        name = self.db.cursor.fetchone()

    def delete_good(self):
        print("Bibop")
        row = self.ui.catalogue_tableWidget_2.currentRow()
        column = self.ui.catalogue_tableWidget_2.currentColumn()
        id = self.ui.catalogue_tableWidget_2.item(row, column).text()

        try:
            self.db.cursor.execute(
            "delete from goods where id='" + id + "' ")
            msgBox = QMessageBox()
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setText("Continue?")
            result = msgBox.exec_()
            if QMessageBox.Yes == result:
                self.db.cnxn.commit()
                self.goods_list_change()
            elif QMessageBox.No == result:
                self.db.cursor.execute(
                    "rollback")
            else:
                print("wtf?")
            self.db.cnxn.commit()
            self.goods_list_change()
        except (Exception, psycopg2.Error) as error:
            self.db.cursor.execute("rollback")
            self.db.cnxn.commit()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('{}'.format(error))
            msg.setInformativeText('На этот товар есть заявки или у него установлен приоритет')
            msg.setWindowTitle("Ошибка")
            msg.exec_()


    def add_button_clicked(self):
        new_name = str(self.ui.good_name_lineEdit.text())
        if not (new_name.isalnum()) and len(new_name) < 3:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Некорректный ввод")
            error_message.showMessage('Введите другое наименование')
        else:
            good_name = new_name
            w1 = int(str(self.ui.w1_lineEdit.text()))
            w2 = int(str(self.ui.w2_lineEdit.text()))
            priority = str(self.ui.priority_lineEdit.text())
            id = int(str(self.ui.id_lineEdit.text()))
            try:
                if priority != '':
                    # self.db.cursor.call("proc",(id, good_name, priority, w1, w2))
                    self.db.cursor.execute("call proc(%s,%s,%s,%s,%s);", (id, good_name, priority, w1, w2))

                else:
                    # self.db.cursor.callproc(" call proc", (id, good_name, w1, w2))
                    self.db.cursor.execute("call proc(%s,%s,%s,%s,%s)", (id, good_name,0.0, w1, w2))

                self.db.cnxn.commit()
                self.goods_list_change()

                print("smth happened")
            except (Exception, psycopg2.Error) as error:
                self.db.cursor.execute("rollback")
                self.db.cnxn.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('{}'.format(error))
                #msg.setInformativeText(error)
                msg.setWindowTitle("Ошибка")
                msg.exec_()

    def goods_list_change(self):
        self.db.cursor.execute(
            "select goods.id,name,w.good_count as warehouse1,w22.good_count as warehouse2,priority from goods left join warehouse1 w on goods.id = w.good_id left join warehouse2 w22 on goods.id = w22.good_id ")
        filler.fillTable(self.ui.catalogue_tableWidget_2, self.db.cursor, 5)

    def show_all_goods(self) :
        self.db.cursor.execute("select goods.id,name,w.good_count as warehouse1,w22.good_count as warehouse2,priority from goods left join warehouse1 w on goods.id = w.good_id left join warehouse2 w22 on goods.id = w22.good_id ")
        filler.fillTable(self.ui.catalogue_tableWidget_2, self.db.cursor, 5)

    def sort_by(self):
        ganre=str(self.ui.ganre_comboBox.currentText())
        self.db.cursor.execute("SELECT songs.name as songs_name, songs.price,songs.upload_date,ganres.name as ganre_name,users.name as artist_name from ((songs inner join ganres on songs.ganre_id = ganres.ganre_id) inner join users on songs.user_id = users.user_id )")
        filler.fillTable(self.ui.songs_catalogue_tableWidget, self.db.cursor, 5)


    def exit_button_clicked(self):
        self.main = sign_in_controller.sign_inWindow()
        self.main.show()
        self.close()



