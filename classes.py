from pico2d import *

images = (load_image('resources\\character\\shipsprite1.png'))


class Object:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = None
        self.speed = 0
        self.size = 0
    pass


class Player:
    def __init__(self):
        self.obj = Object()
    pass


class Enemy:
    def __init__(self):
        self.obj = Object()
        pass
    pass


class Bullet:
    def __init__(self):
        self.obj = Object()
        pass
    pass







