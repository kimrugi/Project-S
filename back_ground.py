from pico2d import *
import random
SIZE_X, SIZE_Y = 8400, 8400

class Star:
    image = None
    def __init__(self, screen):
        if Star.image == None:
            Star.image = load_image("resources\\background\\star.png")
        self.x = random.randint(0, SIZE_X)
        self.y = random.randint(0, SIZE_Y)
        self.size = random.randint(1, 100)

    def get_bb(self):
        return self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size

    def update(self):
        pass

    def draw(self, screen):
        self.image.draw(self.x - screen.x, self.y - screen.y, self.size, self.size)


class Background:
    pass
