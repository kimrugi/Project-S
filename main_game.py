import framework
import game_value
import player_ship
from pico2d import *
import game_world
import back_ground
import paused
import weapon
import screen
import bullet
import default_enemy
import nokkey
import Flatter
import sleeve
import wei

player = None
background = None
player_weapon = None
back_screen = None
enemys = []
bullets = []
delete_list = []
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
    background = load_image('resources\\background\\black.png')
    player = player_ship.Player()
    back_screen = screen.Screen(player)
    player_weapon = weapon.Weapon(player)
    enemy = wei.Wei()
    enemys.append(enemy)
    game_world.add_object(enemy, 1)
    game_world.add_object(player, 1)
    game_world.add_object(back_screen, 1)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            back_screen.lock_screen()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            back_screen.unlock_screen()

        else:
            player.handle_event(event)
            player_weapon.handle_event(event)


def update():
    for o in game_world.all_objects():
        o.update()
    for b in bullets:
        for e in enemys:
            if collide(b, e):
                e.crash_by_bullet(b)
        if collide(player, b):
            player.crash_by_bullet(b)
    for e in enemys:
        if collide(player, e):
            player.crash_by_enemy(e)
    while len(delete_list) > 0:
        d = delete_list.pop()
        game_world.remove_object(d)
        del d
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

def add_bullet(x, y, horizon, vertical, shooter, shoot_speed, damage):
    bul = bullet.Bullet(x, y, horizon, vertical, shooter, shoot_speed, damage)
    bullets.append(bul)
    game_world.add_object(bul, 1)

def add_delete_list(object):
    delete_list.append(object)
    if object in enemys:
        enemys.remove(object)
    elif object in bullets:
        bullets.remove(object)
