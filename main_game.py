import framework
import classes
from pico2d import *

player = None

def init():
    global player
    player = classes.Player()
    pass


def exit():
    global player
    del player
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
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
               framework.quit()
            if event.key == SDLK_w:
                player.add_vertical(1)
            if event.key == SDLK_s:
                player.add_vertical(-1)
            if event.key == SDLK_a:
                player.add_horizon(-1)
            if event.key == SDLK_d:
                player.add_horizon(1)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                player.add_vertical(-1)
            if event.key == SDLK_s:
                player.add_vertical(1)
            if event.key == SDLK_a:
                player.add_horizon(1)
            if event.key == SDLK_d:
                player.add_horizon(-1)


def update():
    player.update()
    pass


def draw():
    clear_canvas()
    player.draw()
    update_canvas()



