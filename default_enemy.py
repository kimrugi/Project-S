from pico2d import *
import math
import main_game
import framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import bullet
import game_world
import HPBar
PIXEL_PER_KILOMETER = 5
QUAD_PI = math.pi / 4
HALF_OF_QUAD_PI = QUAD_PI / 2

LEFT, UP, RIGHT, BOTTOM = 0, 44, 90, 3
IMAGE_WIDTH, IMAGE_HEIGHT = 90, 41
DAMAGED_EFFECT = 0.5

class DefaultEnemy:
    image = None

    def load_image(self):
        if DefaultEnemy.image is None:
            DefaultEnemy.image = load_image('resources\\character\\enemys.png')

    def reset_status(self):
        pass

    def __init__(self, x=4000, y=4000):
        self.x = x
        self.y = y
        self.size = 50
        self.size_propotion = IMAGE_WIDTH / IMAGE_HEIGHT
        self.load_image()
        self.kmps = 5
        self.chase_kmps = 16
        self.speed = None
        self.vertical = 0
        self.horizon = 0
        self.is_effect = 0
        self.effect_time = 0.3
        self.set_speed(self.kmps)
        self.dir = math.pi / 4
        self.detect_range = 100000000
        self.shoot_delay = 0.5
        self.shoot_count = 0
        self.damage_amount = 10
        self.max_HP = 12
        self.HP = self.max_HP
        self.hp_bar = HPBar.HPBar(self)
        self.bt = None
        self.build_behavior_tree()
        self.reset_status()
        pass

    def get_bb(self):
        x_size = self.size * self.size_propotion / 3
        y_size = self.size / 3
        left = self.x - x_size
        up = self.y - y_size
        right = self.x + x_size
        down = self.y + y_size
        return left, up, right, down

    def set_speed(self, kmps):
        self.kmps = kmps
        self.speed = kmps * PIXEL_PER_KILOMETER

    def find_player(self):
        player = main_game.get_player()
        distance = (player.x - self.x) ** 2 + (player.y - self.y) ** 2
        if distance < self.detect_range:
            self.dir = rounds_pi(math.atan2(player.x - self.x, player.y - self.y))
            #self.dir = math.atan2(player.x - self.x, player.y - self.y)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def move_to_player(self):
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Chase", self.move_to_player)
        shoot_to_player = LeafNode("Shoot", self.attack)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node, shoot_to_player)
        self.bt = BehaviorTree(chase_node)

    def attack(self):
        self.shoot_count += framework.frame_time
        if self.shoot_count > self.shoot_delay:
            player = main_game.get_player()
            self.shoot_count -= self.shoot_delay
            Bullet = bullet.Bullet(self.x, self.y, player.x - self.x, player.y - self.y, self)
            game_world.add_object(Bullet, 1)
        return BehaviorTree.SUCCESS

    def update(self):
        self.bt.run()
        self.shoot_count += framework.frame_time
        self.x += self.speed * math.sin(self.dir) * framework.frame_time
        self.y += self.speed * math.cos(self.dir) * framework.frame_time
        pass

    def draw(self, screen):
        DefaultEnemy.image.clip_draw(LEFT, BOTTOM, IMAGE_WIDTH, IMAGE_HEIGHT, self.x - screen.x, self.y - screen.y,
                                     self.size * self.size_propotion, self.size)
        if self.HP > self.max_HP:
            self.hp_bar.draw(screen)

    def get_damaged(self, damage):
        self.HP -= damage
        self.hp_bar.change_hp()
        if self.HP < 0:
            main_game.add_delete_list(self)
            pass

    def crash_by_bullet(self, other):
        if not (self in other.ignore_list):
            self.get_damaged(other.damage)
            main_game.add_delete_list(other)
            return


def rounds_pi(theta):
    rounds = theta + HALF_OF_QUAD_PI
    result = rounds - rounds % QUAD_PI
    return result










