from pico2d import *
import math
import main_game
import framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import bullet
import game_world
import default_enemy
import random
PIXEL_PER_KILOMETER = 5
QUAD_PI = math.pi / 4
HALF_OF_QUAD_PI = QUAD_PI / 2
SEC_PER_ANIMATION = 15


512 / 4
LEFT = [0, 128, 128 * 2, 128 * 3]
BOTTOM = [128 * 3, 128 * 2, 128, 0]

IMAGE_HEIGHT = IMAGE_WIDTH = 128

class Explosion():
    image = None

    def load_image(self):
        if Explosion.image is None:
            Explosion.image = load_image('resources\\character\\explosion.png')

    def __init__(self, x,y,size):
        self.load_image()
        self.frame = 0
        self.frame_count = 0
        self.x, self.y = x, y
        self.size = size * 2
        pass

    def update(self):
        self.frame += framework.frame_time * SEC_PER_ANIMATION
        if self.frame > 15:
            if random.randint(0, 20) == 0:
                main_game.add_upgrade(self.x, self.y)
            main_game.add_delete_list(self)
        pass

    def draw(self, screen):
        self.image.clip_draw(LEFT[int(self.frame) % 4], BOTTOM[int(self.frame) // 4], IMAGE_WIDTH, IMAGE_HEIGHT,
                             self.x - screen.x, self.y - screen.y, self.size, self.size)
