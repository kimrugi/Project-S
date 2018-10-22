from pico2d import *

images = (load_image('resources\\character\\shipsprite1.png'))

image_x, image_y = 192, 512
class test_class:
    def __init__(self):
        self.image = load_image('resources\\character\\shipsprite1.png')
        self.x, self.y = 500, 500
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(0, 0, image_x // 3, image_y // 8, self.x, self.y)

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







