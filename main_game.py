import framework
import player
from pico2d import *
import game_world

player = None

def init():
    global player
    player = Player()
    game_world.add_object(player, 1)
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
               framework.quit()
            else:
                player.handle_event(event)



def update():
    for o in game_world.all_objects():
        o.update()
    pass


def draw():
    clear_canvas()
    for o in game_world.all_objects():
        o.update()
    update_canvas()





