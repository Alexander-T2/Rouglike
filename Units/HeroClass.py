from Desings import path


class Hero:
    starterPoint = 3
    img = f'{path}Images\\HeroSpace.png'

    def __init__(self):
        self.health = 20
        self.spike_walk = False
        self.max_health = 20
        self.damage = 1
        self.cords = [10, 5]
        self.range = 1
        self.speed = 1
        self.score = 0
        self.killed = 0
        self.died = 0
