from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from Desings import path


class Credits(QWidget):
    def __init__(self, main_menu):
        super().__init__()
        self.menu = main_menu
        uic.loadUi(f'{path}Credits.ui', self)
        self.BackButton.clicked.connect(self.go_back)
        self.Vincent.setPixmap(QPixmap(f'{path}Images\\Vincent2.png'))

    def go_back(self):
        self.menu.show()
        self.hide()
