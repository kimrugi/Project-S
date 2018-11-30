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

LEFT, BOTTOM = 185, 0

IMAGE_WIDTH, IMAGE_HEIGHT = 241 - 185, 309 - 254
SIZE_PROPOTION = IMAGE_WIDTH / IMAGE_HEIGHT

SIZE_KM = 7
SPEED_KMPS = 20
MOVE_TIME = 0.5
SPEED_KMPHP = 5

class Wei(default_enemy.DefaultEnemy):
    def load_image(self):
        if Wei.image is None:
            Wei.image = load_image('resources\\character\\enemys.png')

    def reset_status(self):
        self.size = SIZE_KM * PIXEL_PER_KILOMETER
        self.set_speed(SPEED_KMPS)
        self.shoot_delay = 1
        self.damage_amount = 5
        self.HP = 15
        self.size_propotion = SIZE_PROPOTION
        pass

    def find_player(self):
        player = main_game.get_player()
        self.dir = math.atan2(player.x - self.x, player.y - self.y)
        return BehaviorTree.SUCCESS

    def delay_time(self):
        if self.shoot_count > self.shoot_delay:
            self.shoot_count -= self.shoot_delay
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL
        pass

    def build_behavior_tree(self):
        find_player_node = LeafNode("Find Player", self.find_player)
        delay_node = LeafNode("Delay", self.delay_time)
        shoot_to_player = LeafNode("Shoot", self.attack)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, delay_node, shoot_to_player)
        self.bt = BehaviorTree(chase_node)


        pass

    def get_damaged(self, damage):
        self.HP -= damage
        self.set_speed(self.kmps + (damage * SPEED_KMPHP))
        if self.HP < 0:
            main_game.add_delete_list(self)

    def attack(self):
        self.get_damaged(1)
        return BehaviorTree.SUCCESS

    def draw(self, screen):
        self.image.clip_draw(LEFT, BOTTOM, IMAGE_WIDTH, IMAGE_HEIGHT, self.x - screen.x, self.y - screen.y,
                               self.size * SIZE_PROPOTION, self.size)

