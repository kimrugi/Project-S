from pico2d import *
import framework

middle = (framework.GAME_SIZE[0] // 2, framework.GAME_SIZE[1] // 2)
PIXEL_PER_KILOMETER = 1
RADIAN = 3.14159265359 / 4



RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, SPACE_DOWN, SPACE_UP = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}

next_state_table = {}


image_x, image_y = 100, 100


class IdleState:
    @staticmethod
    def enter(player, event):
        player.vertical = 0
        player.horizon = 0
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        player.idle_image.rotate_draw(RADIAN * player.dir, middle[0], middle[1], player.size, player.size)
        pass

dir_table = { (0, 1): 0, (1, 1): 1, (1, 0): 2, (1, -1): 3, (0, -1): 4, (-1, -1): 5, (-1, 0): 6, (-1, 1): 7 }

class MoveState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.horizon += player.speed
        elif event == LEFT_DOWN:
            player.horizon -= player.speed
        elif event == RIGHT_UP:
            player.horizon -= player.speed
        elif event == LEFT_UP:
            player.horizon += player.speed
        elif event == DOWN_DOWN:
            player.vertical -= player.speed
        elif event == UP_DOWN:
            player.vertical += player.speed
        elif event == DOWN_UP:
            player.vertical += player.speed
        elif event == UP_UP:
            player.vertical -= player.speed
        ho = clamp(-1, player.horizon, 1)
        ver = clamp(-1, player.vertical, 1)
        player.dir = dir_table[ho, ver]

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        player.move_image.rotate_draw(RADIAN * player.dir, middle[0], middle[1], player.size, player.size)
        pass


class Player:
    idle_image = None
    move_image = None
    def __init__(self):
        self.x = 100
        self.y = 100
        self.size = 50
        self.dir = 1
        if self.idle_image == None:
            self.idle_image = load_image('resources\\character\\idle_space_ship.png')
        if self.move_image == None:
            self.move_image = load_image('resources\\character\\spaceship.png')
        self.vertical = 0
        self.horizon = 0
        self.event_que = []
        self.kmps = 15
        self.speed = None
        self.calcul_speed(self.kmps)
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def calcul_speed(self, kmps):
        self.kmps = kmps
        self.speed = self.kmps / PIXEL_PER_KILOMETER

    def fire(self):
        pass

    def move(self):
        self.x = self.x + self.horizon * self.speed
        self.y = self.y + self.vertical * self.speed

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.event_que.append(key_event)
        pass

    pass









