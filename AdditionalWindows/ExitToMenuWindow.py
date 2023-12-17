from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from Desings import path


class ToMenuExitWindow(QDialog):
    def __init__(self, field, main_menu):
        super().__init__()
        self.menu = main_menu
        self.field = field
        uic.loadUi(f'{path}ToMenuExitWindow.ui', self)
        self.NoButton.clicked.connect(self.go_back)
        self.YesButton.clicked.connect(self.exit_game)

    def go_back(self):
        self.hide()

    def exit_game(self):  # Не удаётся выйти в меню
        self.menu.show()
        self.field.hide()
        self.hide()

