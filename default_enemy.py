from pico2d import *
import math
import main_game
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

PIXEL_PER_KILOMETER = 5
QUAD_PI = math.pi / 4
HALF_OF_QUAD_PI = QUAD_PI / 2

class DefaultEnemy:
    image = None

    def __init__(self):
        self.x = 100
        self.y = 100
        self.size = 50
        if DefaultEnemy.image is None:
            DefaultEnemy.image = load_image('')
        self.kmps = 16
        self.speed = None
        self.vertical = 0
        self.horizon = 0
        self.calcul_speed(self.kmps)
        self.dir = math.pi
        self.detect_range = 500
        pass

    def calcul_speed(self, kmps):
        self.kmps = kmps
        self.speed = self.kmps * PIXEL_PER_KILOMETER
    pass

    def find_player(self):
        player = main_game.get_player()
        distance = (player.x - self.x) ** 2 + (player.y - self.y) ** 2
        if distance < self.detect_range ** 2:
            self.dir = rounds_pi(math.atan2(player.x - self.x, player.y - self.y))
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    


def rounds_pi(theta):
    result = theta + HALF_OF_QUAD_PI % QUAD_PI
    return result










