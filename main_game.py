import framework
import game_value
import player_ship
from pico2d import *
import game_world
import back_ground
import paused
import weapon
import screen

player = None
background = None
player_weapon = None
back_screen = None

def enter():
    global player, background, player_weapon, back_screen
    player = player_ship.Player()
    game_world.add_object(player, 1)
    background = load_image('resources\\background\\black.png')
    player_weapon = weapon.Weapon(player)
    game_world.add_object(player_weapon, 1)
    back_screen = screen.Screen(player)
    game_world.add_object(back_screen, 0)
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
    background.draw(game_value.middle[0], game_value.middle[1], game_value.WINDOW_SIZE[0], game_value.WINDOW_SIZE[1])
    for o in game_world.all_objects():
        o.draw(back_screen)
    update_canvas()


def get_player():
    return player


