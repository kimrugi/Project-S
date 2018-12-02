import framework
from pico2d import *

import game_value
import game_world
import main_game


WHITE, GRAY = (255, 255, 255), (130, 130, 130)

class SelectItem:
    def __init__(self, effect, order, name=""):
        self.name = name
        self.effect = effect
        self.order = order
        self.selected = 0
        self.color = GRAY
    def draw(self):
        font.draw()


ITEMS = ["FIX SHIP", "RANDOM STAT", "RANDOM "]
NUM_OF_ITEMS = 0

font = None
player = None
space_station = None

def enter():
    global font, player, space_station
    main_game.clear_enemys()
    player = main_game.get_player()
    space_station = main_game.get_SS()
    space_station.resource_amount += player.carrying_resource
    player.carrying_resource = 0
    font = load_font('resources\\text\\kongtext.ttf')
    pass


def exit():
    global font
    del font
    pass


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
                    selection = NUM_OF_ITEMS
                selection -= 1
            if event.key == SDLK_DOWN:
                selection = (selection + 1) % NUM_OF_ITEMS
            if event.key == SDLK_SPACE:
                pass


def update():
    pass


def draw_texts():
    pass


def draw():
    clear_canvas()
    update_canvas()


