from pico2d import *
import framework
from game_value import middle

IMAGE_SIZE = (491, 344)
BULLET_POSITION = -(int(190 - IMAGE_SIZE[1]))
class Bullet:
    image = None
    def __init__(self, weapon):
        self.x = weapon.player.x
        self.y = weapon.player.y
        self.size = 10
        if Bullet.image == None:
            Bullet.image = load_image('resources\\bullet\\bullet1.png')
        self.speed = 200
        self.vertical = weapon.vertical
        self.horizon = weapon.horizon
        pass

    def draw(self, screen):
        self.image.clip_draw(0, BULLET_POSITION, 8, 8, self.x - screen.x, self.y - screen.y, self.size, self.size)
        pass

    def update(self):
        self.x += self.speed * self.horizon * framework.frame_time
        self.y += self.speed * self.vertical * framework.frame_time
        pass
    pass
