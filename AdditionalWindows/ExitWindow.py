import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from Desings import path


class ExitWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(f'{path}ExitWindow.ui', self)
        self.NoButton.clicked.connect(self.go_back)
        self.YesButton.clicked.connect(self.exit_game)

    def go_back(self):
        self.hide()

    def exit_game(self):
        sys.exit()
