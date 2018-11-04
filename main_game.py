import framework
import player_ship
from pico2d import *
import game_world
import back_ground
import paused
import weapon

player = None
background = None
player_weapon = None

def enter():
    global player, background, player_weapon
    player = player_ship.Player()
    game_world.add_object(player, 1)
    background = load_image('resources\\background\\black.png')
    player_weapon = weapon.Weapon(player)
    game_world.add_object(player_weapon, 1)
    for i in range(1000):
        star = back_ground.Star(player)
        game_world.add_object(star, 0)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                framework.push_state(paused)
        else:
            player.handle_event(event)
            player_weapon.handle_event(event)



def update():
    for o in game_world.all_objects():
        o.update()
    pass


def draw():
    clear_canvas()
    background.draw(player_ship.middle[0], player_ship.middle[1], framework.WINDOW_SIZE[0], framework.WINDOW_SIZE[1])
    for o in game_world.all_objects():
        o.draw()
    update_canvas()





