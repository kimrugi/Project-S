from pico2d import *
import main_game
import game_value
import math
class Arrow():
    image = None
    def load_image(self):
        if Arrow.image is None:
            Arrow.image = load_image('resources\\etc\\arrow.png')

    def __init__(self):
        self.load_image()
        self.player = main_game.get_player()
        self.ss = main_game.get_SS()
        self.dir = 0
        pass

    def update(self):
        self.dir = -(math.atan2(self.player.x - self.ss.x, self.player.y - self.ss.y))
        pass

    def get_bb(self):
        return self.player.get_bb()

    def draw(self, screen):
        distance = (self.player.x - self.ss.x) ** 2 + (self.player.y - self.ss.y) ** 2
        if distance > 270 * 270:
            self.image.rotate_draw(self.dir, game_value.middle[0], game_value.middle[1])
