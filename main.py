import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from qt_1 import Ui_mainWindow
import sqlite3
from picther import MainWindow_Picther
from Exeption import Window_Exaption
from add_product import Window_Add
from math import floor
import csv
import subprocess


def counting_cost(cost, sale):
    return sale - cost


def count_percent(wage, p):
    # Проверка на то, что минимальная сумма которую выплатит человек будет минимум 1
    a = wage * (p / 100)
    return a


class MyClass(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # используется для того чтобы пользователь ввел свое имя и товар
        self.name_pol, ok_pressed_pol = QInputDialog.getText(self, "Введите имя покупателя",
                                                             "Имя покупателя:")
        if not ok_pressed_pol:
            sys.exit()
        self.comboBox_name.addItem('Все')
        # кнопка отвечающая за показ товара пользователю
        self.label_sale.setText('0')
        self.label_cost.setText('0')
        self.label_val_cost_2.setText('0')
        self.exaption = Window_Exaption()
        self.pushButton_show.clicked.connect(self.picther_show)

        # радио кнопка отвечающая за общий процент зарплаты сотрудникам

        self.label_procent.setText('25% на зарплату сотрудникам')
        self.radioButton.clicked.connect(self.rb)

        # кнопка подсчета

        self.pushButton_count.clicked.connect(self.count)

        # кнопка сохранение в csv файл
        self.comboBox_name.activated.connect(self.change_val_cost)
        self.pushButton_save.clicked.connect(self.save)
        self.add_p = Window_Add(list_product)
        self.pushButton_add.clicked.connect(self.add_product)
        self.pushButton_list_product.clicked.connect(self.add_product_list)
        self.pushButton_list_product.clicked.connect(self.change_val_cost)
        self.pushButton_change_pol.clicked.connect(self.change_pol)
        self.label_current_user.setText('Пользователь: ' + self.name_pol)

    def change_pol(self):
        subprocess.call([sys.executable, os.path.relpath(__file__)] + sys.argv[1:])

    def change_val_cost(self):
        # Подключаем БД
        con = sqlite3.connect('qt_bd.db')
        cur = con.cursor()
        # выбираем из таблицы стоимость товара
        if self.comboBox_name.currentText() == 'Все':
            sale = 0
            cost = 0
            for index_sale in range(self.comboBox_name.count() - 1):
                product = self.comboBox_name.itemText(index_sale + 1)
                sale_current = cur.execute(f'''
                SELECT sale FROM product WHERE title = '{product}'
                ''')
                sale += list(sale_current)[0][0]
                cost_current = cur.execute(f'''
                SELECT cost FROM product WHERE title = '{product}'
                ''')
                cost += list(cost_current)[0][0]
        else:
            product = self.comboBox_name.itemText(self.comboBox_name.currentIndex())
            sale_current = cur.execute(f'''
                           SELECT sale FROM product WHERE title = '{product}'
                           ''')
            sale = list(sale_current)[0][0]
            cost_current = cur.execute(f'''
                           SELECT cost FROM product WHERE title = '{product}'
                           ''')
            cost = list(cost_current)[0][0]
        # превращаем sqlite в строку
        self.label_sale.setText(str(sale))
        self.label_cost.setText(str(cost))
        self.label_val_cost_2.setText(str(counting_cost(cost, sale)))
        con.commit()
        con.close()

    def add_product_list(self):
        self.name_product, ok_pressed_product = QInputDialog.getItem(self, "Введите имя товара",
                                                                     "Имя товара:", tuple(list_product), 0, False)
        if ok_pressed_product:
            self.comboBox_name.addItem(self.name_product)

    def add_product(self):
        global list_product
        self.add_p.show()
        list_product = self.add_p.list_product

    # функция сохранения
    def save(self):
        if self.label_wages_full_1.text() == '':
            self.label_print.setText('Сначала посчитайте зарплату и расходы')
        else:
            self.wage_1 = round(float(self.label_wages_full_1.text()), 2)
            self.wage_2 = round(float(self.label_wages_full_2.text()), 2)
            self.wage_3 = round(float(self.label_wages_full_3.text()), 2)
            self.wage_b = round(float(self.label_wages_full_b.text()), 2)
            self.wage_d = round(float(self.label_wages_full_d.text()), 2)
            self.expenses_1 = round(count_percent(self.wage_1, 43), 2)
            self.expenses_2 = round(count_percent(self.wage_2, 43), 2)
            self.expenses_3 = round(count_percent(self.wage_3, 43), 2)
            self.expenses_b = round(count_percent(self.wage_b, 43), 2)
            self.expenses_d = round(count_percent(self.wage_d, 43), 2)
            self.remains = round(float(self.lcdNumber_3.value()), 2)
            con = sqlite3.connect('qt_bd.db')
            cur = con.cursor()
            if self.comboBox_name.currentText() == 'Все':
                list_name = []
                for index_sale in range(self.comboBox_name.count() - 1):
                    product = self.comboBox_name.itemText(index_sale + 1)
                    name = cur.execute(f'''
                    SELECT title FROM product WHERE title = '{product}'
                    ''')
                    list_name.append(list(name)[0][0])
                name = ', '.join(list_name)
            else:
                name = self.comboBox_name.currentText()
            # добавление пользователя
            cur.execute(f'''INSERT INTO shopper(men, product, wage_1, wage_2, wage_3, wage_d, wage_b, expenses_1, 
            expenses_2, expenses_3, expenses_b, expenses_d, remains) 
               VALUES("{self.name_pol}", "{name}", "{self.wage_1}", "{self.wage_2}", "{self.wage_3}"
               , "{self.wage_d}", "{self.wage_b}", "{self.expenses_1}", "{self.expenses_2}"
               , "{self.expenses_3}", "{self.expenses_b}", "{self.expenses_d}", "{self.remains}")
                   ''')
            le = len(list(cur.execute('''SELECT men FROM shopper''')))

            # сохранение данных в csv файл

            with open('data/results.csv', 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Покупатель', 'Товар', 'Зарплата 1', 'Зарплата 2', 'Зарплата 3',
                                 'Зарплата Бугалтера', 'Зарплата Директора', 'Расходы 1', 'Расходы 2', 'Расходы 3',
                                 'Расходы Бугалтера', 'Расходы Директора', 'Остаток'])
                for i in range(le):
                    list_bd = list(cur.execute(f"""
                    SELECT men, product, wage_1, wage_2, wage_3, wage_d, wage_b, expenses_1, 
                    expenses_2, expenses_3, expenses_b, expenses_d, remains FROM shopper
                    WHERE id == {i + 1}
                    """))[0]
                    writer.writerow(list_bd)
            con.commit()
            con.close()
            self.label_print.setText('Таблица успешно сохранена')

    # функция подсчитывающая всю зарплату и расходы

    def count(self):
        val = int(self.label_val_cost_2.text())
        sum_wages = val * (self.rb() / 100)

        # проверка на корректные вводные данные

        if not self.lineEdit_count_day_1.text().isdigit():
            self.exaption.show()
            return 0
        if not self.lineEdit_count_day_2.text().isdigit():
            self.exaption.show()
            return 0
        if not self.lineEdit_count_day_3.text().isdigit():
            self.exaption.show()
            return 0
        count_1 = int(self.lineEdit_count_day_1.text())
        if count_1 > 31:
            self.exaption.show()
            return 0
        count_2 = int(self.lineEdit_count_day_2.text())
        if count_2 > 31:
            self.exaption.show()
            return 0
        count_3 = int(self.lineEdit_count_day_3.text())
        if count_3 > 31:
            self.exaption.show()
            return 0

        # подсчет зарплат работников и администрации

        sum_count = sum([count_1, count_2, count_3])
        count_wages_day = round(sum_wages / sum_count, 1)
        wage_1 = floor(count_wages_day * count_1)
        wage_2 = floor(count_wages_day * count_2)
        wage_3 = floor(count_wages_day * count_3)
        wage_d = int(val * 0.15)
        wage_b = int(val * 0.1)

        # показ полное зарплаты без учета уплаты налогов

        self.label_wages_full_1.setText(str(wage_1))
        self.label_wages_full_2.setText(str(wage_2))
        self.label_wages_full_3.setText(str(wage_3))
        self.label_wages_full_d.setText(str(wage_d))
        self.label_wages_full_b.setText(str(wage_b))

        # показ количество рублей пойдущих на НДФЛ

        self.label_ndfl_1.setText(str(round(count_percent(wage_1, 13), 2)))
        self.label_ndfl_2.setText(str(round(count_percent(wage_2, 13), 2)))
        self.label_ndfl_3.setText(str(round(count_percent(wage_3, 13), 2)))
        self.label_ndfl_d.setText(str(round(count_percent(wage_d, 13), 2)))
        self.label_ndfl_b.setText(str(round(count_percent(wage_b, 13), 2)))

        # показ количество рублей пойдущих на ФСС

        self.label_fss_1.setText(str(round(count_percent(wage_1, 2.9), 2)))
        self.label_fss_2.setText(str(round(count_percent(wage_2, 2.9), 2)))
        self.label_fss_3.setText(str(round(count_percent(wage_3, 2.9), 2)))
        self.label_fss_d.setText(str(round(count_percent(wage_d, 2.9), 2)))
        self.label_fss_b.setText(str(round(count_percent(wage_b, 2.9), 2)))

        # показ количество рублей пойдущих на ФОМС

        self.label_foms_1.setText(str(round(count_percent(wage_1, 5.1), 2)))
        self.label_foms_2.setText(str(round(count_percent(wage_2, 5.1), 2)))
        self.label_foms_3.setText(str(round(count_percent(wage_3, 5.1), 2)))
        self.label_foms_d.setText(str(round(count_percent(wage_d, 5.1), 2)))
        self.label_foms_b.setText(str(round(count_percent(wage_b, 5.1), 2)))

        # показ количество рублей пойдущих на ПФР

        self.label_pfr_1.setText(str(round(count_percent(wage_1, 22), 2)))
        self.label_pfr_2.setText(str(round(count_percent(wage_2, 22), 2)))
        self.label_pfr_3.setText(str(round(count_percent(wage_3, 22), 2)))
        self.label_pfr_b.setText(str(round(count_percent(wage_d, 22), 2)))
        self.label_pfr_d.setText(str(round(count_percent(wage_b, 22), 2)))

        # Зарплата которую сотрудники получат на руки

        self.label_wages_out_1.setText(str(round(wage_1 - count_percent(wage_1, 43), 2)))
        self.label_wages_out_2.setText(str(round(wage_2 - count_percent(wage_2, 43), 2)))
        self.label_wages_out_3.setText(str(round(wage_3 - count_percent(wage_3, 43), 2)))
        self.label_wages_out_d.setText(str(round(wage_d - count_percent(wage_d, 43), 2)))
        self.label_wages_out_b_2.setText(str(round(wage_b - count_percent(wage_b, 43), 2)))

        # расходы на комунлку, хозрасходы, амортизацию оборудования

        self.label_amort.setText(str(round(count_percent(val, 1), 2)))
        self.label_com.setText(str(round(count_percent(val, 1), 2)))
        self.label_hoz.setText(str(round(count_percent(val, 1), 2)))
        wage_b = int(self.label_wages_full_b.text())
        wage_d = int(self.label_wages_full_d.text())
        sum_wages += wage_b + wage_d
        self.lcdNumber_1.display(sum_wages)

        # создаем список расходов

        sum_expenses = []

        # добавляем в список расходов все имеющиеся расходы

        sum_expenses.append(self.label_amort.text())
        sum_expenses.append(self.label_hoz.text())
        sum_expenses.append(self.label_com.text())
        sum_expenses.append(self.label_pfr_1.text())
        sum_expenses.append(self.label_pfr_2.text())
        sum_expenses.append(self.label_pfr_3.text())
        sum_expenses.append(self.label_pfr_d.text())
        sum_expenses.append(self.label_pfr_b.text())
        sum_expenses.append(self.label_foms_1.text())
        sum_expenses.append(self.label_foms_2.text())
        sum_expenses.append(self.label_foms_3.text())
        sum_expenses.append(self.label_foms_d.text())
        sum_expenses.append(self.label_foms_b.text())
        sum_expenses.append(self.label_fss_1.text())
        sum_expenses.append(self.label_fss_2.text())
        sum_expenses.append(self.label_fss_3.text())
        sum_expenses.append(self.label_fss_d.text())
        sum_expenses.append(self.label_fss_b.text())
        sum_expenses.append(self.label_ndfl_1.text())
        sum_expenses.append(self.label_ndfl_2.text())
        sum_expenses.append(self.label_ndfl_3.text())
        sum_expenses.append(self.label_ndfl_b.text())
        sum_expenses.append(self.label_ndfl_d.text())

        # каждый элемент списка преобразуем в число

        sum_expenses = list(map(float, sum_expenses))
        sum_expenses = sum(sum_expenses)

        # выводим на экран суммарные расходы

        self.lcdNumber_2.display(sum_expenses)

        # создаем список остатка прибыли

        sum_remains = []
        sum_remains.append(sum_wages)
        sum_remains.append(sum_expenses)
        self.lcdNumber_3.display(val - sum(sum_remains))

    # функция проверяющая состояние радио кнопки

    def rb(self):
        if self.radioButton.isChecked():
            self.label_procent.setText('20% на зарплату сотрудникам')
            return 20
        else:
            self.label_procent.setText('25% на зарплату сотрудникам')
            return 25

    # функция показывающая товар

    def picther_show(self):
        name = self.comboBox_name.currentText()
        if name == 'Все':
            self.exaption.show()
        else:
            self.show_product = MainWindow_Picther(name)
            self.show_product.show()


con = sqlite3.connect('qt_bd.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
title TEXT,
cost  INTEGER,
sale  INTEGER);''')
list_product = []
[list_product.append(i[0]) for i in list(cur.execute('''
        SELECT title FROM product
        '''))]
if 'Ноутбук' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Ноутбук", 30000, 40000)''')
if 'Монитор' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Монитор", 15000, 20000)''')
if 'Оперативная память' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Оперативная память", 1500, 2000)''')
if 'Видео карта' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Видео карта", 30000, 40000)''')
if 'Блок питания' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Блок питания", 5000, 6000)''')
if 'Жесткий диск' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Жесткий диск", 2500, 3000)''')
if 'Сетевая карта' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Сетевая карта", 500, 700)''')
if 'Звуковая карта' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Звуковая карта", 2500, 3000)''')
if 'Системный блок' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Системный блок", 25000, 30000)''')
if 'Мышь' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Мышь", 500, 800)''')
if 'Процессор' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Процессор", 10000, 15000)''')
if 'Клавиатура' not in list_product:
    cur.execute('''INSERT INTO product(title, cost, sale)
    VALUES("Клавиатура", 1500, 2000)''')
cur.execute('''CREATE TABLE IF NOT EXISTS shopper (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
men TEXT,
product  TEXT
wage_1 INTEGER
wage_2 INTEGER
wage_3 INTEGER
wage_d INTEGER
wage_b INTEGER
expenses_1 INTEGER
expenses_2 INTEGER
expenses_3 INTEGER
expenses_b INTEGER
expenses_d INTEGER
remains INTEGER);''')
con.commit()
con.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyClass()
    ex.show()
    sys.exit(app.exec_())
