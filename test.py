
from pico2d import *
import framework


name = "Test"


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


