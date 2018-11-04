from pico2d import *
import framework
import back_ground
middle = (framework.WINDOW_SIZE[0] // 2, framework.WINDOW_SIZE[1] // 2)
IMAGE_SIZE = (491, 344)
BULLET_POSITION = -(int(190 - IMAGE_SIZE[1]))
class Bullet:
    image = None
    player = None
    def __init__(self, weapon):
        self.x = weapon.player.x
        self.y = weapon.player.y
        self.size = 10
        if self.image == None:
            self.image = load_image('resources\\bullet\\bullet1.png')
        if self.player == None:
            self.player = weapon.player
        self.speed = 200
        self.vertical = weapon.vertical
        self.horizon = weapon.horizon
        pass

    def draw(self):
        self.image.clip_draw(0, BULLET_POSITION, 8, 8, self.x - self.player.x + middle[0], self.y - self.player.y + middle[1], self.size, self.size)
        pass

    def update(self):
        self.x += self.speed * self.horizon * framework.frame_time
        self.y += self.speed * self.vertical * framework.frame_time
        pass
    pass
