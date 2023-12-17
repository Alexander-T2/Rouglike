import random

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel
from Desings import path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from Units.HeroClass import Hero
from Units.Enemies import Enemy, RangedEnemy, Chest, Hole
from Generator.FieldGenerator import RoomGenerator
from AdditionalWindows.DeadMenu import DeadMenu
from AdditionalWindows.ExitToMenuWindow import ToMenuExitWindow


class FieldWidget(QWidget):
    def __init__(self, main_menu):
        super().__init__()
        self.main_menu = main_menu
        self.ToMenuExitWindow = ToMenuExitWindow(self, main_menu)
        uic.loadUi(f'{path}GameField.ui', self)
        self.doors_opened = False
        self.diff = None
        self.flag = True
        self.counter = 0
        self.speed_counter = 0
        self.stuff = ['boots', 'leggings', 'armor', 'helmet', 'sword']
        self.room = [[[QLabel(self)] for _ in range(11)] for _ in range(11)]
        self.realHero = None
        self.roomData = None
        self.x1 = None
        self.x2 = None
        self.xdir = None
        self.y1 = None
        self.y2 = None
        self.ydir = None
        self.new_stuff = None
        self.x = 0
        self.y = 0
        self.h = 72
        self.w = 72
        self.turn = True
        for i in range(11):
            for j in range(11):
                spc = self.room[i][j][0]
                spc.setText("")
                spc.setGeometry(self.x, self.y, self.w, self.h)
                self.x += 72
            self.x = 0
            self.y += 72
        self.ToMenuButton.clicked.connect(self.to_menu)

    def use(self, roomData):
        if len(roomData) == 2:
            self.diff = roomData[1]
            roomData = roomData[0]
        try:
            for i in range(11):
                for j in range(11):  # attaching images to Labels
                    if roomData[i][j][0] == 0:
                        img = f'{path}Images\\EmptySpace.png'
                    else:
                        if isinstance(roomData[i][j][0], Hero):
                            self.realHero = roomData[i][j][0]
                            self.realHero.cords = roomData[i][j][0]
                        img = roomData[i][j][0].img
                        roomData[i][j][0].cords = [i, j]
                    self.room[i][j][0].setPixmap(QPixmap(img))
        except Exception as e:  # remove later
            print(type(e), e)
        self.roomData = roomData  # Unit info
        self.ScoreLineWidget.setText(f'{self.realHero.score}P')
        self.HealthLineWidget.setText(f'{self.realHero.health}HP')
        if self.realHero.health <= 0:
            self.main_menu.new_game_counter = 0
            self.Ded = DeadMenu(self.main_menu, self.realHero.killed, self.realHero.died, self.realHero.score)
            self.Ded.show()
            self.hide()

    def keyPressEvent(self, event):  # Hero's turn
        self.x1 = self.realHero.cords[0]
        self.y1 = self.realHero.cords[1]
        self.flag = True

        if event.key() == Qt.Key_W:
            self.x2 = self.realHero.cords[0] - 1
            self.y2 = self.realHero.cords[1]

        elif event.key() == Qt.Key_X:
            self.x2 = self.realHero.cords[0] + 1
            self.y2 = self.realHero.cords[1]

        elif event.key() == Qt.Key_D:
            self.x2 = self.realHero.cords[0]
            self.y2 = self.realHero.cords[1] + 1

        elif event.key() == Qt.Key_A:
            self.x2 = self.realHero.cords[0]
            self.y2 = self.realHero.cords[1] - 1

        elif event.key() == Qt.Key_E:
            self.x2 = self.realHero.cords[0] - 1
            self.y2 = self.realHero.cords[1] + 1

        elif event.key() == Qt.Key_C:
            self.x2 = self.realHero.cords[0] + 1
            self.y2 = self.realHero.cords[1] + 1

        elif event.key() == Qt.Key_Z:
            self.x2 = self.realHero.cords[0] + 1
            self.y2 = self.realHero.cords[1] - 1

        elif event.key() == Qt.Key_Q:
            self.x2 = self.realHero.cords[0] - 1
            self.y2 = self.realHero.cords[1] - 1

        else:
            self.flag = False
        try:
            if self.x2 >= 0 and self.y2 >= 0 and self.flag:
                try:
                    if self.roomData[self.x2][self.y2][0] == 0:
                        self.roomData[self.x2][self.y2][0] = self.realHero
                        self.roomData[self.x1][self.y1][0] = 0

                    elif isinstance(self.roomData[self.x2][self.y2][0], Enemy) \
                            or isinstance(self.roomData[self.x2][self.y2][0], RangedEnemy):
                        self.roomData[self.x2][self.y2][0].health -= self.realHero.damage

                    elif isinstance(self.roomData[self.x2][self.y2][0], Chest):
                        self.roomData[self.x2][self.y2][0] = self.realHero
                        self.roomData[self.x1][self.y1][0] = 0
                        if len(self.stuff) != 0:
                            self.new_stuff = random.choice(self.stuff)
                            if self.new_stuff == 'boots':
                                self.stuff.remove('boots')
                                self.realHero.spike_walk = True
                                self.BootsLabelWidget.setPixmap(QPixmap(f'{path}Images\\NewBootsLabelWidget.png'))
                            elif self.new_stuff == 'leggings':
                                self.stuff.remove('leggings')
                                self.realHero.speed += 1
                                self.PantsLabelWidget.setPixmap(QPixmap(f'{path}Images\\NewPantsLabelWidgwet.png'))
                            elif self.new_stuff == 'armor':
                                self.stuff.remove('armor')
                                self.realHero.max_health += 4
                                self.realHero.health += 4
                                self.ArmorLabelWidget.setPixmap(QPixmap(f'{path}Images\\NewArmorLabelWidget.png'))
                            elif self.new_stuff == 'helmet':
                                self.stuff.remove('helmet')
                                self.realHero.max_health += 2
                                self.realHero.health += 2
                                self.HelmetLabelWidget.setPixmap(QPixmap(f'{path}Images\\NewHelmetLabelWidget.png'))
                            else:
                                self.stuff.remove('sword')
                                self.realHero.damage += 1  # change Hero's image
                                self.realHero.img = f'{path}Images\\HeroSwordSpace.png'
                                self.WeaponLabelWidget.setPixmap(QPixmap(f'{path}Images\\SwordLabelWidget.png'))
                        else:
                            self.realHero.health += 1
                        self.realHero.score += 25
                        print("Chest opened (+25P)")

                    elif isinstance(self.roomData[self.x2][self.y2][0], Hole):
                        if not self.realHero.spike_walk:
                            self.realHero.health -= 1

                    else:
                        pass  # Wrong Button pressed
                    if self.doors_opened is True:  # leaving a room
                        if (self.x2, self.y2) in ((0, 5), (5, 10), (10, 5), (5, 0)):
                            self.realHero.cords = [self.x2, self.y2]
                            self.realHero.health = self.realHero.max_health
                            self.doors_opened = False
                            self.speed_counter = 0
                            self.roomData = RoomGenerator(self.diff, self.realHero).make_room()
                    self.use(self.roomData)  # Add death
                    self.speed_counter += 1
                    if self.flag:
                        if self.speed_counter == self.realHero.speed:
                            self.speed_counter = 0
                            self.enemy_turn()

                except IndexError:  # Hero's turn again
                    pass
        except Exception as e:
            print(type(e), e)

    def enemy_turn(self):
        self.counter = 0
        for i in range(11):
            for j in range(11):
                if isinstance(self.roomData[i][j][0], Enemy):  # swordsman
                    self.counter += 1
                    if self.roomData[i][j][0].health <= 0:
                        self.roomData[i][j][0] = 0
                        self.realHero.died += 1
                        self.realHero.killed += 1
                        print("Guardian fell and died (+100P)")
                        self.realHero.score += 100
                        continue
                    if not self.roomData[i][j][0].angry:  # if not angry it wonders around
                        self.xdir = i + random.randint(-1, 1)
                        self.ydir = j + random.randint(-1, 1)
                        if abs(self.realHero.cords[0] - i) < 3 and abs(self.realHero.cords[1] - j) < 3:
                            self.roomData[i][j][0].angry = True
                    else:  # chases hero if angry
                        if self.realHero.cords[0] > self.roomData[i][j][0].cords[0]:
                            self.xdir = i + 1
                        elif self.realHero.cords[0] < self.roomData[i][j][0].cords[0]:
                            self.xdir = i - 1
                        else:
                            self.xdir = i
                        if self.realHero.cords[1] > self.roomData[i][j][0].cords[0]:
                            self.ydir = j + 1
                        elif self.realHero.cords[1] < self.roomData[i][j][0].cords[0]:
                            self.ydir = i - 1
                        else:
                            self.ydir = j
                    try:
                        checker = self.ydir >= 0 and self.xdir >= 0  # so they don't teleport
                        # to opposite side of the map
                        if self.roomData[self.xdir][self.ydir][0] == 0 and checker:
                            self.roomData[self.xdir][self.ydir][0] = self.roomData[i][j][0]
                            self.roomData[i][j][0] = 0
                        elif isinstance(self.roomData[self.xdir][self.ydir][0], Hole) and checker:
                            self.roomData[i][j][0] = 0
                            self.realHero.died += 1
                            print("Guardian fell and died (+100P)")
                            self.realHero.score += 100
                        elif isinstance(self.roomData[self.xdir][self.ydir][0], Hero) and checker:
                            self.realHero.health -= 1
                    except IndexError:  # Then he chooses to do nothing
                        pass
                elif isinstance(self.roomData[i][j][0], RangedEnemy):  # archer
                    self.counter += 1
                    if self.roomData[i][j][0].health <= 0:
                        self.roomData[i][j][0] = 0
                        self.realHero.died += 1
                        self.realHero.killed += 1
                        print("Archer-dog died (+130P)")
                        self.realHero.score += 130
                        continue
                    if not self.roomData[i][j][0].angry:  # if not angry it wonders around
                        self.xdir = i + random.randint(-1, 1)
                        self.ydir = j + random.randint(-1, 1)
                        if abs(self.realHero.cords[0] - i) < 3 and abs(self.realHero.cords[1] - j) < 3:
                            self.roomData[i][j][0].angry = True
                    else:
                        if random.randint(-1, 1):  # will either shoot or flee if angry
                            if abs(self.realHero.cords[0] - i) < 3 and abs(self.realHero.cords[1] - j) < 2:
                                self.realHero.health -= 1
                                continue  # If it shoots it won't move
                        if self.realHero.cords[0] > self.roomData[i][j][0].cords[0]:
                            self.xdir = i - 1
                        elif self.realHero.cords[0] < self.roomData[i][j][0].cords[0]:
                            self.xdir = i + 1
                        else:
                            self.xdir = i
                        if self.realHero.cords[1] > self.roomData[i][j][0].cords[0]:
                            self.ydir = j - 1
                        elif self.realHero.cords[1] < self.roomData[i][j][0].cords[0]:
                            self.ydir = i + 1
                        else:
                            self.ydir = j

                    try:
                        checker = self.ydir >= 0 and self.xdir >= 0
                        if self.roomData[self.xdir][self.ydir][0] == 0 and checker:
                            self.roomData[self.xdir][self.ydir][0] = self.roomData[i][j][0]
                            self.roomData[i][j][0] = 0
                        elif isinstance(self.roomData[self.xdir][self.ydir][0], Hole) and checker:
                            self.roomData[i][j][0] = 0
                            print("Archer-dog fell and died (+130P)")
                            self.realHero.died += 1
                            self.realHero.score += 130
                    except IndexError:  # Then he chooses to do nothing
                        pass
                    else:
                        pass
        if self.counter == 0:  # if no enemies are left the doors will open
            self.doors_opened = True
        self.use(self.roomData)

    def to_menu(self):
        self.ToMenuExitWindow.show()
