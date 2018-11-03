import framework
from pico2d import *
import game_world
import main_game
import main_menu


NUM_OF_MENUS = 3

RESUME_GAME, GO_TO_MAINMENU, QUIT_GAME = range(NUM_OF_MENUS)


selection = RESUME_GAME

selection_table = {
    
    }

def enter():
    
    pass


def exit():
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
                elif selection == GO_TO_MAINMENU:
                    framework.delete_all_and_change(main_menu)
                elif selection == QUIT_GAME:
                    framework.quit()
                    

def update():
    
    pass


def draw():
    clear_canvas()
    main_game.draw()
    update_canvas()








