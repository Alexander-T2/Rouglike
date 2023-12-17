import random

from Units.HeroClass import Hero
from Units.Enemies import Enemy, RangedEnemy, Hole, Chest


class RoomGenerator:
    def __init__(self, difficulty, hero=Hero()):  # Amount of objects in a room
        self.difficulty = difficulty
        if self.difficulty == "easy":
            self.enemies = random.randrange(4, 6)  # Amount of enemies in a room
            self.stuff = random.randrange(5, 9)  # Amount of objects in a room
            self.ranged_enemies = False  # will there be archers or won't
            self.ranged_enemie = 0
            self.chest_counter = 1
        elif self.difficulty == "medium":
            self.enemies = random.randrange(3, 4)
            self.ranged_enemie = random.randrange(2, 3)
            self.stuff = random.randrange(5)
            self.ranged_enemies = True
            self.chest_counter = 1
        else:
            self.enemies = 20
            self.stuff = 0
            self.ranged_enemies = True
            self.chest_counter = 1
        self.size = 11
        self.hero = hero

    def make_room(self):  # Making random room
        cells_to_occupie = 121
        room = [[[0] for _ in range(11)] for _ in range(11)]  # Feeling the room
        if self.ranged_enemies is True:
            additional_unit = RangedEnemy()
        else:
            additional_unit = Enemy()
        for i in range(11):
            for j in range(11):
                cells_to_occupie -= 1
                if not ([i, j] in [[0, 5], [5, 0], [10, 5], [5, 10]]):
                    if self.enemies == 0 and self.stuff == 0:
                        break
                    elif self.enemies + self.stuff + self.ranged_enemie >= cells_to_occupie:  # If space is small
                        if random.randint(0, 1) and self.enemies != 0:
                            unit = random.choice([Enemy(), Enemy(), Hole()])  # Choosing an enemy
                            self.enemies -= 1
                        elif self.stuff != 0:
                            unit = Hole()
                            self.stuff -= 1
                        elif self.ranged_enemie != 0:
                            unit = RangedEnemy()
                        elif self.chest_counter != 0:
                            unit = Chest()
                        else:
                            unit = 0
                        room[i][j][0] = unit
                        unit = 0
                    else:
                        if random.randint(1, 100) > 90:
                            if random.randint(0, 1) and self.enemies != 0:
                                unit = random.choice([Enemy(), Enemy(), additional_unit])  # Choosing an enemy
                                self.enemies -= 1
                            elif self.stuff != 0:
                                unit = Hole()
                                self.stuff -= 1
                            elif self.ranged_enemie != 0:
                                unit = RangedEnemy()
                            else:
                                if self.chest_counter > 0:
                                    unit = Chest()
                                    self.chest_counter -= 1
                                else:
                                    unit = 0
                            room[i][j][0] = unit
                            unit = 0
        if self.hero.score == 0:
            room[10][5][0] = Hero()
        else:
            print(self.hero.cords)
            if self.hero.cords == [10, 5]:
                room[1][5][0] = Chest()
                room[0][5][0] = self.hero
            elif self.hero.cords == [5, 0]:
                room[5][9][0] = Chest()
                room[5][10][0] = self.hero
            elif self.hero.cords == [0, 5]:
                room[10][6][0] = Chest()
                room[10][5][0] = self.hero
            else:
                room[5][1][0] = Chest()
                room[5][0][0] = self.hero

        return room, self.difficulty
