import framework
from pico2d import *

import game_value
import game_world
import main_game

NUM_OF_MENUS = 2

START_GAME, QUIT_GAME = range(NUM_OF_MENUS)


selection = START_GAME



texts = None
selection = 0
font = None
background = None
music = None
def enter():
    global texts, selection, font, background, music
    texts = load_image("resources\\text\\main menu.png")
    font = load_font('resources\\text\\kongtext.ttf')
    selection = START_GAME
    background = load_image('resources\\background\\menu.png')
    music = load_music('resources\\music\\menu.mp3')
    music.set_volume(20)
    music.repeat_play()

def exit():
    global texts, font, background, music
    del texts
    del font
    del background
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

font_location = [(game_value.WINDOW_SIZE[0] // 2 - 300, game_value.WINDOW_SIZE[1] // 2),
                 (game_value.WINDOW_SIZE[0] // 2 - 300, game_value.WINDOW_SIZE[1] // 2 - 150)]

def draw():
    clear_canvas()
    background.draw(game_value.middle[0], game_value.middle[1], game_value.WINDOW_SIZE[0], game_value.WINDOW_SIZE[1])
    font.draw(font_location[selection][0], font_location[selection][1], "->", (255, 255, 255))
    texts.clip_draw(0, 200, 500, 100, game_value.WINDOW_SIZE[0] // 2, game_value.WINDOW_SIZE[1] // 2)
    texts.clip_draw(0, 0, 500, 100, game_value.WINDOW_SIZE[0] // 2, game_value.WINDOW_SIZE[1] // 2 - 150)
    update_canvas()


