from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt


class Window_Exaption(QMainWindow):
    def __init__(self):
        super(Window_Exaption, self).__init__()
        self.setWindowTitle('ОШИБКА')
        self.label = QLabel(self)
        self.label.setText('Ошибка!!!')
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)
        self.label.setStyleSheet("background-color: rgb(255, 0, 0);")
