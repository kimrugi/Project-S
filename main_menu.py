import framework
from pico2d import *
import game_world
import main_game

texts = None


def init():
    global texts
    texts = load_image("resources\\text\\main menu.png")
    pass


def exit():
    global texts
    del texts


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
    global texts
    clear_canvas()
    texts.clip_draw(0, 200, 500, 100, framework.GAME_SIZE[0] // 2, framework.GAME_SIZE[1] // 2 + 100)
    texts.clip_draw(0, 100, 500, 100, framework.GAME_SIZE[0] // 2, framework.GAME_SIZE[1] // 2 )
    texts.clip_draw(0, 0, 500, 100, framework.GAME_SIZE[0] // 2, framework.GAME_SIZE[1] // 2 - 100)
    update_canvas()


