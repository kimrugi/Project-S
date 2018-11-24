from pico2d import *
import math
import main_game
import framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import bullet
import game_world
PIXEL_PER_KILOMETER = 5
QUAD_PI = math.pi / 4
HALF_OF_QUAD_PI = QUAD_PI / 2

LEFT, UP, RIGHT, BOTTOM = 0, 44, 90, 3
IMAGE_WIDTH, IMAGE_HEIGHT = 90, 41



class DefaultEnemy:
    image = None

    def load_image(self):
        if DefaultEnemy.image is None:
            DefaultEnemy.image = load_image('resources\\character\\enemys.png')

    def reset_status(self):
        pass

    def __init__(self):
        self.x = 4000
        self.y = 4000
        self.size = 50
        self.load_image()
        self.kmps = 5
        self.chase_kmps = 16
        self.speed = None
        self.vertical = 0
        self.horizon = 0
        self.calcul_speed(self.kmps)
        self.dir = math.pi / 4
        self.detect_range = 500
        self.shoot_speed = 0.5
        self.shoot_delay = 0
        self.bt = None
        self.build_behavior_tree()
        self.reset_status()
        pass

    def calcul_speed(self, kmps):
        self.speed = kmps * PIXEL_PER_KILOMETER

    def find_player(self):
        player = main_game.get_player()
        distance = (player.x - self.x) ** 2 + (player.y - self.y) ** 2
        if distance < self.detect_range ** 2:
            self.dir = rounds_pi(math.atan2(player.x - self.x, player.y - self.y))
            #self.dir = math.atan2(player.x - self.x, player.y - self.y)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def move_to_player(self):
        self.calcul_speed(self.chase_kmps)
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Chase", self.move_to_player)
        shoot_to_player = LeafNode("Shoot", self.attack)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node, shoot_to_player)
        self.bt = BehaviorTree(chase_node)

    def attack(self):
        self.shoot_delay += framework.frame_time
        if self.shoot_delay > self.shoot_speed:
            player = main_game.get_player()
            self.shoot_delay -= self.shoot_speed
            Bullet = bullet.Bullet(self.x, self.y, player.x - self.x, player.y - self.y, self)
            game_world.add_object(Bullet, 1)
        return BehaviorTree.SUCCESS

    def update(self):
        self.bt.run()
        self.x += self.speed * math.sin(self.dir) * framework.frame_time
        self.y += self.speed * math.cos(self.dir) * framework.frame_time
        pass

    def draw(self, screen):
        DefaultEnemy.image.clip_draw(LEFT, BOTTOM, IMAGE_WIDTH, IMAGE_HEIGHT, self.x - screen.x, self.y - screen.y, self.size * 2, self.size)

def rounds_pi(theta):
    rounds = theta + HALF_OF_QUAD_PI
    result = rounds - rounds % QUAD_PI
    return result










