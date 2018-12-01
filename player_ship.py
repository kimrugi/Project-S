from pico2d import *
import framework
import back_ground
from game_value import middle
import math
import main_game
import HPBar
import game_world
PIXEL_PER_KILOMETER = 5
RADIAN = 3.14159265359 / 4

TURNING_SPEED_PER_SECOND = math.pi / 10

RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP = range(8)
DAMAGED_EFFECT = 0.5
SPEED_PER_TON = 1

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_w): UP_DOWN,
    (SDL_KEYDOWN, SDLK_s): DOWN_DOWN,
    (SDL_KEYUP, SDLK_d): RIGHT_UP,
    (SDL_KEYUP, SDLK_a): LEFT_UP,
    (SDL_KEYUP, SDLK_w): UP_UP,
    (SDL_KEYUP, SDLK_s): DOWN_UP,
}

next_state_table = {}

IMAGE_X, IMAGE_Y = 80 - 12, 80 - 18


class IdleState:
    @staticmethod
    def enter(player, event):
        #player.vertical = 0
        #player.horizon = 0
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player, screen):
        player.image.clip_composite_draw(310, 820, IMAGE_X, IMAGE_Y, RADIAN * player.dir, '', player.x - screen.x, player.y - screen.y, player.size,
                                         player.size)
        pass

dir_table = { (0, 1): 0, (1, 1): 1, (1, 0): 2, (1, -1): 3, (0, -1): 4, (-1, -1): 5, (-1, 0): 6, (-1, 1): 7 }

class MoveState:
    @staticmethod
    def enter(player, event):

        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.x += player.horizon * player.speed * framework.frame_time
        player.y += player.vertical * player.speed * framework.frame_time
        player.x = clamp(middle[0], player.x, back_ground.SIZE_X - middle[0])
        player.y = clamp(middle[1], player.y, back_ground.SIZE_Y - middle[1])
        pass

    @staticmethod
    def draw(player, screen):
        player.image.clip_composite_draw(12, 920, IMAGE_X, IMAGE_Y, RADIAN * player.dir, '', player.x - screen.x,
                                         player.y - screen.y, player.size, player.size)
        pass


class Player:
    image = None
    def __init__(self):
        self.x = 4200
        self.y = 4200
        self.max_HP = 50
        self.HP = self.max_HP
        self.size = 50
        self.to_dir = 1
        if Player.image == None:
            Player.image = load_image('resources\\character\\spaceship.png')
        self.vertical = 0
        self.horizon = 0
        self.dir = 0
        self.is_invincible = 0
        self.invincible_time = 0.5
        self.event_que = []
        self.hp_bar = HPBar.HPBar(self)
        self.carrying_resource = 0
        self.kmps = 30
        self.speed = None
        self.calcul_speed(self.kmps)
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def calcul_speed(self, kmps):
        self.kmps = kmps
        self.speed = self.kmps * PIXEL_PER_KILOMETER - self.carrying_resource * SPEED_PER_TON * PIXEL_PER_KILOMETER

    def get_bb(self):
        half_size = self.size / 2
        return self.x - half_size, self.y - half_size, self.x + half_size, self.y + half_size

    def move(self):
        self.x = self.x + self.horizon * self.speed
        self.y = self.y + self.vertical * self.speed

    def turn_to(self):
        self.dir += math.pi

        pass

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            if event == RIGHT_DOWN:
                self.horizon += 1
            if event == LEFT_DOWN:
                self.horizon -= 1
            if event == RIGHT_UP:
                self.horizon -= 1
            if event == LEFT_UP:
                self.horizon += 1
            if event == DOWN_DOWN:
                self.vertical -= 1
            if event == UP_DOWN:
                self.vertical += 1
            if event == DOWN_UP:
                self.vertical += 1
            if event == UP_UP:
                self.vertical -= 1
            if (self.horizon, self.vertical) != (0, 0):
                self.dir = dir_table[self.vertical, self.horizon]
            self.to_dir = math.atan2(self.horizon, self.vertical)
            self.cur_state.exit(self, event)
            if self.horizon == 0 and self.vertical == 0:
                self.cur_state = IdleState
            else:
                self.cur_state = MoveState
            self.cur_state.enter(self, event)
        if self.is_invincible:
            if get_time() - self.damaged_time > 0.5:
                self.image.opacify(1)
                self.is_invincible = 0

    def draw(self, screen):
        self.cur_state.draw(self, screen)
        if self.HP != self.max_HP:
            self.hp_bar.draw(screen)

    def size_up(self, size):
        self.size += size

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.event_que.append(key_event)
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_l):
            self.size_up(2)
        pass

    def damaged_effect(self):
        self.image.opacify(DAMAGED_EFFECT)
        self.damaged_time = get_time()
        self.is_invincible = 1
        pass

    def get_damaged(self, damage):
        if not self.is_invincible:
            self.HP -= damage
            self.damaged_effect()
            self.hp_bar.change_hp()
            if self.HP < 0:
                main_game.add_delete_list(self)

    def crash_by_enemy(self, other):
        self.get_damaged(other.damage_amount)
        pass

    def crash_by_bullet(self, other):
        if not (self in other.ignore_list):
            self.get_damaged(other.damage)
            main_game.add_delete_list(other)

    def give_resource(self, amount):
        self.carrying_resource += amount
    pass









