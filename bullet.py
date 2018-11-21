from pico2d import *
import framework
import math

IMAGE_SIZE = (491, 344)
BULLET_POSITION = -(int(190 - IMAGE_SIZE[1]))
class Bullet:
    image = None

    def __init__(self, x, y, horizon, vertical, shooter):
        self.x = x
        self.y = y
        self.size = 10
        if Bullet.image == None:
            Bullet.image = load_image('resources\\bullet\\bullet1.png')
        self.ignore_list = [shooter]
        self.speed = 200
        self.dir = math.atan2(horizon, vertical)
        pass

    def draw(self, screen):
        self.image.clip_draw(0, BULLET_POSITION, 8, 8, self.x - screen.x, self.y - screen.y, self.size, self.size)
        pass

    def update(self):
        self.x += self.speed * math.sin(self.dir) * framework.frame_time
        self.y += self.speed * math.cos(self.dir) * framework.frame_time
        pass
    pass
