from pico2d import *
import framework
import random
SIZE_X, SIZE_Y = 8400, 8400
middle = (framework.WINDOW_SIZE[0] // 2, framework.WINDOW_SIZE[1] // 2)

650, 587

class Star:
    image = None
    player = None
    def __init__(self, player):
        if Star.image == None:
            Star.image = load_image("resources\\background\\star.png")
        if Star.player == None:
            Star.player = player
        self.x = random.randint(0, SIZE_X)
        self.y = random.randint(0, SIZE_Y)
        self.size = random.randint(1, 100)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x - self.player.x, self.y - self.player.y, self.size, self.size)



class Main_back:
    def __init__(self, player):
        self.image = load_image("resources\\background\\main_background1.png")
        self.x = SIZE_X // 2
        self.y = SIZE_Y // 2
        self.player = player
    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(int(self.player.x - middle[0]), int(self.player.y - middle[1]), framework.WINDOW_SIZE[0], framework.WINDOW_SIZE[1], middle[0], middle[1])










