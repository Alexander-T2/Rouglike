import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from Desings import path


class DeadMenu(QWidget):
    def __init__(self, main_menu, a=1, b=1, c=1):
        super().__init__()
        uic.loadUi(f'{path}DeadMenu.ui', self)
        self.menu = main_menu
        self.DeadMenuButton.clicked.connect(self.go_back)
        self.DeadExitGameButton.clicked.connect(self.exit_game)
        self.KilledLine.setText(f'    killed: {a}')
        self.DiedLine.setText(f'    died: {b}')
        self.ScoreLine.setText(f'    score: {c}')
        self.PictureLabel.setPixmap(QPixmap(f'{path}Images\\PictureLabel.png'))

    def go_back(self):
        self.menu.show()
        self.hide()

    def exit_game(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DeadMenu()
    ex.show()
    sys.exit(app.exec_())
