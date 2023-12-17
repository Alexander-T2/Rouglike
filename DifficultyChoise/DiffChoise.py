from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from Generator.GeneratorConnector import FieldWidget
from Generator.FieldGenerator import RoomGenerator
from Desings import path


class DiffWidget(QWidget):
    def __init__(self, main_menu):
        super().__init__()
        uic.loadUi(f'{path}DifficultyChoise.ui', self)
        self.OpenField = FieldWidget(main_menu)
        self.ez_counter = 0
        self.med_counter = 0
        self.imp_counter = 0
        self.EasyButton.clicked.connect(lambda: self.to_play("easy"))
        self.MediumButton.clicked.connect(lambda: self.to_play("medium"))
        self.ImpossibleButton.clicked.connect(lambda: self.to_play("impossible"))

    def to_play(self, arg):
        if self.ez_counter == 0 and arg == "easy":
            self.ez_counter += 1
            self.med_counter = 0
            self.imp_counter = 0
            self.Description.setText("     It's very hard to die")
        elif self.med_counter == 0 and arg == "medium":
            self.ez_counter = 0
            self.med_counter += 1
            self.imp_counter = 0
            self.Description.setText("    Just as I've intended")
        elif self.imp_counter == 0 and arg == "impossible":
            self.ez_counter = 0
            self.med_counter = 0
            self.imp_counter += 1
            self.Description.setText("      ~Speaks for itself~")
        else:
            room = RoomGenerator(arg).make_room()
            self.OpenField.use(room)
            self.hide()
            self.OpenField.show()
