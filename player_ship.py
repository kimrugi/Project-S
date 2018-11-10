from pico2d import *
import framework
import back_ground

middle = (framework.WINDOW_SIZE[0] // 2, framework.WINDOW_SIZE[1] // 2)
PIXEL_PER_KILOMETER = 5
RADIAN = 3.14159265359 / 4



RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP = range(8)

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
        player.image.clip_composite_draw(300, 800, 100, 100, RADIAN * player.dir, '', middle[0], middle[1], player.size,
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
        player.x += player.horizon * framework.frame_time
        player.y += player.vertical * framework.frame_time
        player.x = clamp(middle[0], player.x, back_ground.SIZE_X - middle[0])
        player.y = clamp(middle[1], player.y, back_ground.SIZE_Y - middle[1])
        pass

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(0, 900, 100, 100, RADIAN * player.dir, '', middle[0], middle[1], player.size, player.size)
        pass


class Player:
    image = None
    def __init__(self):
        self.x = 4200
        self.y = 4200
        self.size = 50
        self.dir = 1
        if Player.image == None:
            Player.image = load_image('resources\\character\\spaceship.png')
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
        self.speed = self.kmps * PIXEL_PER_KILOMETER

    def fire(self):
        pass

    def move(self):
        self.x = self.x + self.horizon * self.speed
        self.y = self.y + self.vertical * self.speed

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            if event == RIGHT_DOWN:
                self.horizon += self.speed
            if event == LEFT_DOWN:
                self.horizon -= self.speed
            if event == RIGHT_UP:
                self.horizon -= self.speed
            if event == LEFT_UP:
                self.horizon += self.speed
            if event == DOWN_DOWN:
                self.vertical -= self.speed
            if event == UP_DOWN:
                self.vertical += self.speed
            if event == DOWN_UP:
                self.vertical += self.speed
            if event == UP_UP:
                self.vertical -= self.speed
            ho = clamp(-1, self.horizon, 1)
            ver = clamp(-1, self.vertical, 1)
            if (ho, ver) != (0, 0):
                self.dir = dir_table[ver, ho]
            self.cur_state.exit(self, event)
            if self.horizon == 0 and self.vertical == 0:
                self.cur_state = IdleState
            else:
                self.cur_state = MoveState
            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self)

    def size_up(self, size):
        self.size += size

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.event_que.append(key_event)
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_l):
            self.size_up(2)
        pass

    pass









