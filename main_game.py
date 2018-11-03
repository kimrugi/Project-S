import framework
import player_ship
from pico2d import *
import game_world
import back_ground
import paused

player = None
background = None
def enter():
    global player, background
    player = player_ship.Player()
    game_world.add_object(player, 1)
    background = back_ground.Main_back()
    game_world.add_object(background, 0)
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
                framework.push_state(paused)
            else:
                player.handle_event(event)



def update():
    for o in game_world.all_objects():
        o.update()
    pass


def draw():
    clear_canvas()
    for o in game_world.all_objects():
        o.draw()
    update_canvas()





