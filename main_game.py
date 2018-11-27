import framework
import game_value
import player_ship
from pico2d import *
import game_world
import back_ground
import paused
import weapon
import screen
import default_enemy
import nokkey
import Flatter
player = None
background = None
player_weapon = None
back_screen = None
enemys = []

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global player, background, player_weapon, back_screen, enemys
    player = player_ship.Player()
    game_world.add_object(player, 1)
    background = load_image('resources\\background\\black.png')
    player_weapon = weapon.Weapon(player)
    game_world.add_object(player_weapon, 1)
    enemy = nokkey.Nokkey()
    enemys.append(enemy)
    game_world.add_object(enemy, 1)
    enemy = Flatter.Flatter()
    enemys.append(enemy)
    game_world.add_object(enemy, 1)
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
    for e in enemys:
        if collide(player, e):
            player.crash_by(e)
    pass


def draw():
    clear_canvas()
    background.draw(game_value.middle[0], game_value.middle[1], game_value.WINDOW_SIZE[0], game_value.WINDOW_SIZE[1])
    for o in game_world.all_objects():
        o.draw(back_screen)
    update_canvas()


def get_player():
    return player


def add_enemys(enemy):
    enemys.append(enemy)
