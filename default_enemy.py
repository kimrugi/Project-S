from pico2d import *
import math

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
        pass
    def calcul_speed(self, kmps):
        self.kmps = kmps
        self.speed = self.kmps * PIXEL_PER_KILOMETER
    pass





def rounds_pi(theta):
    result = theta + HALF_OF_QUAD_PI % QUAD_PI
    return result