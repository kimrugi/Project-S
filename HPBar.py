import math
import main_game
import framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import bullet
import game_world
import default_enemy
from pico2d import *

class HPBar():
    red = None
    back_image = None
    def load_image(self):
        if HPBar.red is None:
            HPBar.red = load_image('resources\\etc\\hp_red.png')
        if HPBar.back_image is None:
            HPBar.back_image = load_image('resources\\etc\\hp_bar_back.png')

    def __init__(self, obj):
        self.load_image()
        self.obj = obj
        self.hp_per = 1
        pass

    def change_hp(self):
        self.hp_per = self.obj.HP / self.obj.max_HP
        pass

    def draw(self, screen):
        self.back_image.draw()
        self.red.draw()
