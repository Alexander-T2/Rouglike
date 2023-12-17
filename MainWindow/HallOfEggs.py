from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from Desings import path


class EggsHall(QWidget):
    def __init__(self, main_menu):
        super().__init__()
        self.menu = main_menu
        uic.loadUi(f'{path}HallOfEggs.ui', self)
        self.BackButton.clicked.connect(self.go_back)
        self.Helmet.setPixmap(QPixmap(f'{path}Images\\NewHelmetLabelWidget.png'))
        self.Armor.setPixmap(QPixmap(f'{path}Images\\NewArmorLabelWidget.png'))
        self.Pants.setPixmap(QPixmap(f'{path}Images\\NewPantsLabelWidgwet.png'))
        self.Boots.setPixmap(QPixmap(f'{path}Images\\NewBootsLabelWidget.png'))
        self.Sword.setPixmap(QPixmap(f'{path}Images\\SwordLabelWidget.png'))
        self.BadArmor.setPixmap(QPixmap(f'{path}Images\\ArmorLabelWidget.png'))
        self.EmptySpace.setPixmap(QPixmap(f'{path}Images\\EmptySpace.png'))
        self.Chest.setPixmap(QPixmap(f'{path}Images\\ChestSpace.png'))
        self.Hole.setPixmap(QPixmap(f'{path}Images\\HoleSpace.png'))
        self.Enemy.setPixmap(QPixmap(f'{path}Images\\EnemySpace.png'))
        self.RangedEnemy.setPixmap(QPixmap(f'{path}Images\\RangedEnemySpace.png'))

    def go_back(self):
        self.menu.show()
        self.hide()
