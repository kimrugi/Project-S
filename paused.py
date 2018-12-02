import framework
from pico2d import *
import game_world
import main_game
import main_menu
import game_value

NUM_OF_MENUS = 1

RESUME_GAME = 0


selection = RESUME_GAME

selection_table = {
    
    }

paused = None

def enter():
    global paused
    paused = load_image('resources\\background\\paused.png')
    pass


def exit():
    global paused
    del paused
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
                    selection = NUM_OF_MENUS
                selection -= 1
            if event.key == SDLK_DOWN:
                selection = (selection + 1) % NUM_OF_MENUS
            if event.key == SDLK_SPACE:
                if selection == RESUME_GAME:
                    framework.pop_state()
                    

def update():
    
    pass


def draw():
    clear_canvas()
    main_game.background.draw(game_value.middle[0], game_value.middle[1], game_value.WINDOW_SIZE[0], game_value.WINDOW_SIZE[1])
    for o in game_world.all_objects():
        if main_game.collide(o, main_game.back_screen):
            o.draw(main_game.back_screen)
    paused.draw(game_value.middle[0], game_value.middle[1], game_value.WINDOW_SIZE[0], game_value.WINDOW_SIZE[1])
    update_canvas()








