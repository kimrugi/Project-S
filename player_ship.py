from pico2d import *



RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,  SPACE_DOWN, SPACE_UP = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}


image_x, image_y = 192, 512


class IdleState:
    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass


class MoveState:
    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass


class Player:
    image = None
    def __init__(self):
        self.x = 100
        self.y = 100
        self.size = 0
        if self.image == None:
            self.image = load_image('resources\\character\\player.png')
        self.speed = 0.2
        self.vertical = 0
        self.horizon = 0
        self.event_que = []

    def move(self):
        self.x = self.x + self.horizon * self.speed
        self.y = self.y + self.vertical * self.speed

    def update(self):
        self.move()
        pass

    def draw(self):
        self.image.clip_draw(0, 0, image_x // 3, image_y // 8, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.event_que.append(key_event)
        pass

    pass









