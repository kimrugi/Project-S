from pico2d import *


class IdleState:
    @staticmethod
    def enter(player, event):
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        pass


class ShootState:
    @staticmethod
    def enter(player, event):
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        pass


dir_table = { (0, 1): 0, (1, 1): 1, (1, 0): 2, (1, -1): 3, (0, -1): 4, (-1, -1): 5, (-1, 0): 6, (-1, 1): 7 }

class Weapon:
    image = None
    player = None
    def __init__(self, player):
        self.dir = 0
        self.fire_rate = 0.1
        if self.image == None:
            self.image = load_image('resources\\character\\weapon.png')
        if self.player == None:
            self.player = player


    def fire(self):
        pass

    def draw(self):
        pass
    pass
