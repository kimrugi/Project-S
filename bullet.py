from pico2d import *
import framework
import math
import main_game

IMAGE_SIZE = (491, 344)
BULLET_POSITION = -(int(190 - IMAGE_SIZE[1]))
class Bullet:
    image = None
    sound = None
    def __init__(self, x, y, ran, horizon, vertical, shooter, shoot_speed, damage):
        self.x = x
        self.y = y
        self.size = damage * 3
        self.damage = damage
        if Bullet.image == None:
            Bullet.image = load_image('resources\\bullet\\bullet1.png')
        if Bullet.sound is None:
            Bullet.sound = load_wav('resources\\SE\\laser shoot.wav')
            Bullet.sound.set_volume(10)
        self.ignore_list = [shooter]
        self.range = ran
        self.decrease_speed = self.size / self.range
        self.speed = shoot_speed + shooter.speed
        self.dir = math.atan2(horizon, vertical)
        self.sound.play()
        pass

    def get_bb(self):
        half_size = self.size / 2
        left = self.x - half_size
        up = self.y - half_size
        right = self.x + half_size
        down = self.y + half_size
        return left, up, right, down

    def draw(self, screen):
        self.image.clip_draw(0, BULLET_POSITION, 8, 8, self.x - screen.x, self.y - screen.y, self.size, self.size)
        pass

    def update(self):
        self.x += self.speed * math.sin(self.dir) * framework.frame_time
        self.y += self.speed * math.cos(self.dir) * framework.frame_time
        self.size -= self.decrease_speed * framework.frame_time
        if self.size < 0:
            main_game.add_delete_list(self)
        pass
    pass
