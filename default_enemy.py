from pico2d import *
import math
import main_game
import framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

PIXEL_PER_KILOMETER = 5
QUAD_PI = math.pi / 4
HALF_OF_QUAD_PI = QUAD_PI / 2

LEFT, UP, RIGHT, BOTTOM = 0, 11, 90, 51



class DefaultEnemy:
    image = None

    def __init__(self):
        self.x = 4000
        self.y = 4000
        self.size = 50
        if DefaultEnemy.image is None:
            DefaultEnemy.image = load_image('resources\\character\\enemys.png')
        self.kmps = 5
        self.chase_kmps = 16
        self.speed = None
        self.vertical = 0
        self.horizon = 0
        self.calcul_speed(self.kmps)
        self.dir = math.pi / 4
        self.detect_range = 500
        self.bt = None
        self.build_behavior_tree()
        pass

    def calcul_speed(self, kmps):
        self.speed = kmps * PIXEL_PER_KILOMETER

    def find_player(self):
        player = main_game.get_player()
        distance = (player.x - self.x) ** 2 + (player.y - self.y) ** 2
        if distance < self.detect_range ** 2:
            #self.dir = rounds_pi(math.atan2(player.x - self.x, player.y - self.y))
            self.dir = math.atan2(player.x - self.x, player.y - self.y)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def move_to_player(self):
        self.calcul_speed(self.chase_kmps)
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Chase", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)
        self.bt = BehaviorTree(chase_node)

    def update(self):
        self.bt.run()
        self.x += self.speed * math.cos(self.dir) * framework.frame_time
        self.y += self.speed * math.sin(self.dir) * framework.frame_time
        pass

    def draw(self, screen):
        DefaultEnemy.image.clip_draw(LEFT, UP, RIGHT, BOTTOM, self.x - screen.x, self.y - screen.y, self.size * 2, self.size)

def rounds_pi(theta):
    result = (theta - HALF_OF_QUAD_PI) % QUAD_PI
    return result










