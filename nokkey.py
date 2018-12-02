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
        self.max_HP = 12
        self.HP = 12
        self.size_propotion = SIZE_PROPOTION
        self.detect_range = 350 * 350
        pass

    def build_behavior_tree(self):
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Chase", self.move_to_player)
        is_near_player_node = LeafNode("is near", self.is_near_player)
        shoot_to_player = LeafNode("Shoot", self.attack)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node, is_near_player_node, shoot_to_player)
        self.bt = BehaviorTree(chase_node)

    def attack(self):
        if self.shoot_count > self.shoot_delay:
            player = main_game.get_player()
            self.shoot_count = 0
            main_game.add_bullet(self.x, self.y, player.x - self.x, player.y - self.y, self, 200, self.damage_amount)
        return BehaviorTree.SUCCESS
        pass

    def draw(self, screen):
        Nokkey.image.clip_draw(LEFT, BOTTOM, IMAGE_WIDTH, IMAGE_HEIGHT, self.x - screen.x, self.y - screen.y,
                               self.size * SIZE_PROPOTION, self.size)
        if self.HP < self.max_HP:
            self.hp_bar.draw(screen)


    pass
