import game_world
import main_game
import math
import framework
import random
import sleeve
import wei
import nokkey
SIZE_X, SIZE_Y = 8400, 8400

PIXEL_PER_KILOMETER = 5
SCREEN_MOVE_SPEED = 300
WINDOW_SIZE = (960, 540)
MIDDLE = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
r = 0

def circle(ox, oy, t, c):
    x = ox + math.cos(t) * c
    y = oy + math.sin(t) * c
    return x, y

class Spawner:
    screen = None
    player = None
    enemys = None

    def __init__(self, player, screen, enemys):
        if Spawner.screen is None:
            Spawner.screen = screen
        if Spawner.player is None:
            Spawner.player = player
        if Spawner.enemys is None:
            Spawner.enemys = enemys
        pass

    def get_bb(self):
        return 0, 0, 0, 0

    def update(self):
        if len(self.enemys) < self.player.carrying_resource / 20:
            self.spawn_enemy()
        pass

    def spawn_enemy(self):
        global r
        e = None
        r = random.randint(0, 10000) / 100
        x, y = circle(self.screen.x + MIDDLE[0], self.screen.y + MIDDLE[1], r, 700)
        r = random.randint(0, 2)
        if r == 0:
            e = nokkey.Nokkey(x, y)
        elif r == 1:
            e = sleeve.Sleeve(x, y)
        elif r == 2:
            e = wei.Wei(x, y)
        main_game.add_enemys(e)
        game_world.add_object(e, 1)

    def draw(self, screen):
        pass



