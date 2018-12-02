import game_world
import main_game
import math
import framework
import random
import sleeve
import wei
import nokkey
import Flatter
from pico2d import *
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
    main_music = None
    boss_music = None
    def __init__(self, player, screen, enemys):
        if Spawner.screen is None:
            Spawner.screen = screen
        if Spawner.player is None:
            Spawner.player = player
        if Spawner.enemys is None:
            Spawner.enemys = enemys
        if Spawner.main_music is None:
            Spawner.main_music = load_music('resources\\music\\main theme.mp3')
            Spawner.main_music.set_volume(20)
        if Spawner.boss_music is None:
            Spawner.boss_music = load_music('resources\\music\\boss.mp3')
            Spawner.boss_music.set_volume(30)
        self.boss = None
        self.current_music = self.main_music

    def play_music(self):
        self.current_music.repeat_play()

    def del_music(self):
        self.current_music.stop()
        del self.current_music
        del Spawner.boss_music
        del Spawner.main_music

    def get_bb(self):
        return 0, 0, 0, 0

    def update(self):
        if self.boss is None:
            if len(self.enemys) < self.player.carrying_resource / 20:
                self.spawn_enemy()
        else:
            if len(self.enemys) < 7:
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

    def del_boss(self):
        self.boss = None
        self.current_music = self.main_music
        self.play_music()

    def spawn_boss(self):
        self.screen.lock_screen()
        self.boss = Flatter.Flatter(self.screen.x + 1000, self.screen.y + 1000)
        main_game.add_enemys(self.boss)
        game_world.add_object(self.boss, 1)
        self.current_music = self.boss_music
        self.play_music()

        pass

    def draw(self, screen):
        pass



