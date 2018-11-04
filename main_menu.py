import framework
from pico2d import *
import game_world
import main_game

NUM_OF_MENUS = 2

START_GAME, QUIT_GAME = range(NUM_OF_MENUS)


selection = START_GAME



texts = None
selection = 0

def init():
    global texts, selection
    texts = load_image("resources\\text\\main menu.png")
    selection = START_GAME


def exit():
    global texts
    del texts


def pause():
    pass


def resume():
    pass


def handle_events():
    global selection
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
               framework.pop_state()
            if event.key == SDLK_UP:
                if selection == 0:
                    selection = NUM_OF_MENUS
                selection -= 1
            if event.key == SDLK_DOWN:
                selection = (selection + 1) % NUM_OF_MENUS
            if event.key == SDLK_SPACE:
                if selection == START_GAME:
                    framework.change(main_game)
                elif selection == QUIT_GAME:
                    framework.quit()

def update():
    
    pass


def draw_texts():
    global texts
    if selection == START_GAME:
        texts.clip_draw(0, 200, 500, 100, framework.WINDOW_SIZE[0] // 2, framework.WINDOW_SIZE[1] // 2)
    texts.clip_draw(0, 0, 500, 100, framework.WINDOW_SIZE[0] // 2, framework.WINDOW_SIZE[1] // 2 - 150)

def draw():
    global texts
    clear_canvas()
    texts.clip_draw(0, 200, 500, 100, framework.WINDOW_SIZE[0] // 2, framework.WINDOW_SIZE[1] // 2)
    texts.clip_draw(0, 0, 500, 100, framework.WINDOW_SIZE[0] // 2, framework.WINDOW_SIZE[1] // 2 - 150)
    update_canvas()


