import framework
from pico2d import *

import game_value
import game_world
import main_game
import main_menu

texts = None
selection = 0
font = None
music = None
background = None
WINDOW_SIZE = (960, 540)
MIDDLE = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
TEXT_X, TEXT_Y = MIDDLE[0], WINDOW_SIZE[1] / 10

def enter():
    global texts, selection, font, music, background
    texts = load_image("resources\\background\\dead.png")
    background = load_image('resources\\background\\black.png')
    font = load_font('resources\\text\\kongtext.ttf')
    music = load_music('resources\\music\\dead.mp3')
    music.set_volume(20)
    music.repeat_play()


def exit():
    global texts, font, background, music
    del background
    del texts
    del font
    music.stop()
    del music


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
                framework.quit()
            elif event.key == SDLK_SPACE:
                framework.change(main_menu)


def update():
    pass


def draw():
    clear_canvas()
    background.draw(game_value.middle[0], game_value.middle[1], game_value.WINDOW_SIZE[0], game_value.WINDOW_SIZE[1])
    texts.draw(game_value.middle[0], game_value.middle[1], game_value.WINDOW_SIZE[0], game_value.WINDOW_SIZE[1])
    font.draw(TEXT_X - ((len("PRESS SPACE") / 2) * 20), TEXT_Y, "PRESS SPACE", (255, 255, 255))
    update_canvas()

