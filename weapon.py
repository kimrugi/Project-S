from pico2d import *
import framework

RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP = range(8)

key_event_table = {(SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
 }


class IdleState:
    @staticmethod
    def enter(player, event):
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        pass


class ShootState:
    @staticmethod
    def enter(player, event):
        player.fire_timer = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.fire_timer += framework.frame_time
        if player.fire_timer > player.fire_rate:
            player.fire_timer -= player.fire_rate
            player.fire()
        pass


dir_table = { (0, 1): 0, (1, 1): 1, (1, 0): 2, (1, -1): 3, (0, -1): 4, (-1, -1): 5, (-1, 0): 6, (-1, 1): 7 }

class Weapon:
    image = None
    player = None
    def __init__(self, player):
        self.dir = 0
        self.fire_rate = 0.1
        self.fire_timer = 0
        self.horizon = 0
        self.vertical = 0
        if self.image == None:
            self.image = load_image('resources\\character\\weapon.png')
        if self.player == None:
            self.player = player


    def fire(self):
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
        self.cur_state.exit(self, event)
        if self.horizon == 0 and self.vertical == 0:
            self.cur_state = IdleState
        else:
            self.cur_state = ShootState
        self.cur_state.enter(self, event)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.event_que.append(key_event)

    def draw(self):
        pass
    pass
