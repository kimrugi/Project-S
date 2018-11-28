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

LEFT, BOTTOM = 104, 3

IMAGE_WIDTH, IMAGE_HEIGHT = 172 - 104, 306 - 257
SIZE_PROPOTION = IMAGE_WIDTH / IMAGE_HEIGHT


class Nokkey(default_enemy.DefaultEnemy):
    def load_image(self):
        if Nokkey.image is None:
            Nokkey.image = load_image('resources\\character\\enemys.png')

    def reset_status(self):
        self.size = 25
        self.set_speed(20)
        self.shoot_delay = 3
        self.damage_amount = 5
        self.HP = 12
        self.size_propotion = SIZE_PROPOTION
        pass

    def attack(self):
        self.shoot_count += framework.frame_time
        if self.shoot_count > self.shoot_delay:
            player = main_game.get_player()
            self.shoot_count -= self.shoot_delay
            main_game.add_bullet(self.x, self.y, player.x - self.x, player.y - self.y, self, 500, self.damage_amount)
        return BehaviorTree.SUCCESS
        pass

    def draw(self, screen):
        Nokkey.image.clip_draw(LEFT, BOTTOM, IMAGE_WIDTH, IMAGE_HEIGHT, self.x - screen.x, self.y - screen.y,
                               self.size * SIZE_PROPOTION, self.size)


    pass
