from pico2d import *

class Enemy:
    image = None

    def __init__(self):
        self.x = 100
        self.y = 100
        self.size = 0
        if Enemy.image is None:
            Enemy.image = load_image('')
        self.speed = 0.2
        self.vertical = 0
        self.horizon = 0
        pass
    pass
