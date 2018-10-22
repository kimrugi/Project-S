import framework
import classes
from pico2d import *

player = None

def init():
    global player
    player = classes.Player()
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
    player.update()
    pass


def draw():
    clear_canvas()
    player.draw()
    update_canvas()



