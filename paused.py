import framework
from pico2d import *
import game_world
import main_game

RESUME_GAME, QUIT_GAME = range(2)


selection = RESUME_GAME

def init():
    
    pass


def exit():
    game_world.clear()
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
               framework.pop_state()


def update():
    
    pass


def draw():
    clear_canvas()
    main_game.draw()
    update_canvas()








