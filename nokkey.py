from pico2d import *
import math
import main_game
import framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import bullet
import game_world
import default_enemy
PIXEL_PER_KILOMETER = 5
QUAD_PI = math.pi / 4
HALF_OF_QUAD_PI = QUAD_PI / 2

LEFT, BOTTOM = 100, 0
IMAGE_WIDTH, IMAGE_HEIGHT = 76, 56
SIZE_PROPOTION = IMAGE_WIDTH / IMAGE_HEIGHT


class Nokkey(default_enemy.DefaultEnemy):
    def load_image(self):
        if Nokkey.image is None:
            Nokkey.image = load_image('resources\\character\\enemys.png')

    def reset_status(self):
        self.size = 25
        pass

    def attack(self):
        self.shoot_delay += framework.frame_time
        if self.shoot_delay > self.shoot_speed:
            player = main_game.get_player()
            self.shoot_delay -= self.shoot_speed
            Bullet = bullet.Bullet(self.x, self.y, player.x - self.x, player.y - self.y, self)
            game_world.add_object(Bullet, 1)
        return BehaviorTree.SUCCESS
        pass

    def draw(self, screen):
        Nokkey.image.clip_draw(LEFT, BOTTOM, IMAGE_WIDTH, IMAGE_HEIGHT, self.x - screen.x, self.y - screen.y,
                               self.size * SIZE_PROPOTION, self.size)


    pass
