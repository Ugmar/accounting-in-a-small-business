from PyQt5.QtWidgets import QMainWindow, QLabel
from add import Ui_MainWindow
import sqlite3


class Window_Add(QMainWindow, Ui_MainWindow):
    def __init__(self, list_product):
        super().__init__()
        self.list_product = list_product
        self.setupUi(self)
        self.pushButton_save.clicked.connect(self.add_product)

    def add_product(self):
        self.name = self.lineEdit_name.text()

        # Проверка на корректные введенные данные

        try:
            self.sale = int(self.lineEdit_sale.text())
            self.cost = int(self.lineEdit_cost.text())
            if self.cost < self.sale and self.cost > 0 and self.sale > 0:
                con = sqlite3.connect('qt_bd.db')
                cur = con.cursor()
                # добавляем в список все товары
                if self.name in self.list_product:
                    self.label_print.setText('Этот товар уже есть в списке')
                else:
                    cur.execute(f'''INSERT INTO product(title, cost, sale)
                                VALUES("{self.name}", "{self.cost}", "{self.sale}")''')
                    self.label_print.setText('Товар успешно добавлен')
                    self.list_product.append(self.name)
                con.commit()
                con.close()
            else:
                self.label_print.setText('Введите удовлетворящие цены(выручка должна быть больше)')
        except:
            self.label_print.setText('Введите цену числами')
