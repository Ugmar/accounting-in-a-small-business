from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton


class MainWindow_Picther(QMainWindow):

    def __init__(self, name):
        super(MainWindow_Picther, self).__init__()
        list_photo = ['Блок питания', 'Видео карта', 'Жесткий диск', 'Звуковая карта', 'Клавиатура', 'Монитор',
                      'Мышь', 'Ноутбук', 'Оперативная память', 'Процессор', 'Сетевая карта', 'Системный блок']
        self.title = "Товар"
        self.setWindowTitle(self.title)
        label = QLabel(self)
        self.setCentralWidget(label)
        self.name = name
        if self.name not in list_photo:
            label.setText("Извините, но данного товара нет в списке возможно отображаемых")
        else:
            label = QLabel(self)
            pixmap = QPixmap(f'data\{self.name}.jpg')
            label.setPixmap(pixmap)
            self.setCentralWidget(label)
            self.resize(pixmap.width(), pixmap.height())
