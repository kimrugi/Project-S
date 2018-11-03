from pico2d import *
import framework
SIZE_X, SIZE_Y = 1920, 1080
middle = (framework.GAME_SIZE[0] // 2, framework.GAME_SIZE[1] // 2)

class Main_back:
    def __init__(self):
        self.image = load_image("resources\\background\\main_background.png")
        self.x = SIZE_X // 2
        self.y = SIZE_Y // 2

    def update(self):
        pass

    def draw(self):
        self.image.draw(middle[0], middle[1], framework.GAME_SIZE[0], framework.GAME_SIZE[1])










