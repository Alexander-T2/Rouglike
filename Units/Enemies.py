from Desings import path


class Enemy:
    img = f'{path}Images\\EnemySpace.png'

    def __init__(self):  # Stats
        self.health = 3
        self.damage = 1
        self.angry = False


class RangedEnemy:
    img = f'{path}Images\\RangedEnemySpace.png'

    def __init__(self):  # Stats
        self.health = 2
        self.damage = 1
        self.angry = False


class Hole:
    img = f'{path}Images\\HoleSpace.png'


class Chest:
    img = f'{path}Images\\ChestSpace.png'
