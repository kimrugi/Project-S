from pico2d import *
import math
import main_game
import framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import bullet
import game_world
import default_enemy
import nokkey
PIXEL_PER_KILOMETER = 5
QUAD_PI = math.pi / 4
HALF_OF_QUAD_PI = QUAD_PI / 2

LEFT, UP, RIGHT, BOTTOM = 0, 44, 90, 3
IMAGE_WIDTH, IMAGE_HEIGHT = 90, 41


class Flatter(default_enemy.DefaultEnemy):

    def reset_status(self):
        self.set_speed(10)
        pass

    def attack(self):
        self.shoot_count += framework.frame_time
        if self.shoot_count > self.shoot_speed:
            self.shoot_count -= self.shoot_speed
            self.spawn_nokkeys()

    def spawn_nokkeys(self):
        nok = nokkey.Nokkey(self.x - IMAGE_HEIGHT / 2, self.y - IMAGE_HEIGHT / 2)
        game_world.add_object(nok, 1)
        pass

    def draw(self, screen):
        Flatter.image.clip_draw(LEFT, BOTTOM, IMAGE_WIDTH, IMAGE_HEIGHT, self.x - screen.x, self.y - screen.y,
                                     self.size * 2, self.size)


    pass
