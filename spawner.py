import game_value
import main_game
import math
import framework
SIZE_X, SIZE_Y = 8400, 8400

PIXEL_PER_KILOMETER = 5
SCREEN_MOVE_SPEED = 300
WINDOW_SIZE = (960, 540)
MIDDLE = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)


class Spawner:
    screen = None

    def __init__(self, screen):
        if Spawner.screen is None:
            Spawner.screen = screen
        self.x = screen.x
        self.y = screen.y
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass



