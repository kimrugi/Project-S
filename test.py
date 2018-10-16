
from pico2d import *
import framework


class test_class:
    def __init__(self):
        self.image = load_image('resources\\character\\shipsprite1.png')
        self.x, self.y = 500, 500


def enter():
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
               framework.quit()


def update():
    pass


def draw():
   pass


