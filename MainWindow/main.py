import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from DifficultyChoise.DiffChoise import DiffWidget
from AdditionalWindows.ExitWindow import ExitWindow
from MainWindow.HallOfEggs import EggsHall
from MainWindow.Credits import Credits
from Desings import path


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.new_game_counter = 0
        self.NewGameWindow = DiffWidget(self)
        self.OpenField = self.NewGameWindow.OpenField
        self.ExitMenu = ExitWindow()
        self.Eggs = EggsHall(self)
        self.Credits = Credits(self)
        uic.loadUi(f'{path}MainLayout.ui', self)
        self.NewGameButton.clicked.connect(self.new_game)
        self.ContinueButton.clicked.connect(self.continue_game)
        self.EggsButton.clicked.connect(self.eggs)
        self.CreditsButton.clicked.connect(self.credits)
        self.ExitButton.clicked.connect(self.exit_game)

    def new_game(self):
        """Leads to difficulty choice"""
        self.hide()
        self.new_game_counter += 1
        self.NewGameWindow.show()  # Leads to DifficultyChoice

    def continue_game(self):
        """Loading save"""
        if self.new_game_counter > 0:
            self.hide()
            self.OpenField.show()
        else:
            pass

    def eggs(self):
        """Game Info"""
        self.Eggs.show()
        self.hide()

    def credits(self):
        """Credits"""
        self.Credits.show()
        self.hide()

    def exit_game(self):
        """Exit's the game"""
        self.ExitMenu.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
