from pico2d import *
import framework
SIZE_X, SIZE_Y = 9600, 5400
middle = (framework.GAME_SIZE[0] // 2, framework.GAME_SIZE[1] // 2)

class Main_back:
    def __init__(self, player):
        self.image = load_image("resources\\background\\main_background.png")
        self.x = SIZE_X // 2
        self.y = SIZE_Y // 2
        self.player = player
    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.player.x - middle[0], self.player.y - middle[1], framework.GAME_SIZE[0], framework.GAME_SIZE[1])










