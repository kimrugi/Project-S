from pico2d import *
import default_enemy
import random
import main_game
import framework


DAMAGE, RANGE, SHOOT_SPEED, SHOOT_DELAY, MAX_HP, SPEED, MIN_DELAY = range(7)

stat_text_table = {DAMAGE:"DAMAGE UP", RANGE:"RANGE UP", SHOOT_SPEED:"SHOOT SPEED UP", SHOOT_DELAY:"FIRE RATE UP",
                   MAX_HP:"MAX HP UP", SPEED:"SPEED UP", MIN_DELAY: "FIRE RATE LIMITE DOWN"}

class UpgradeUnit():
    image = None

    def __init__(self, x, y):
        self.load_image()
        self.x, self.y = x, y
        self.stat = None
        self.speed = random.randint(10, 40) / 20
        self.size = 20
        self.set_stat()
        self.dir = random.randint(-500, 500) / 500


    def set_stat(self):
        self.stat = random.randint(0, 5)

    def load_image(self):
        if UpgradeUnit.image is None:
            UpgradeUnit.image = load_image('resources\\etc\\astro.png')

    def get_bb(self):
        half_size = self.size / 2
        return self.x - half_size, self.y - half_size, self.x + half_size, self.y + half_size

    def crash(self, player):
        if self.stat == DAMAGE:
            player.weapon.damage_amount += 1
        elif self.stat == RANGE:
            player.weapon.range += 1
        elif self.stat == SPEED:
            player.calcul_speed(player.kmps + 1)
        elif self.stat == SHOOT_SPEED:
            player.weapon.shoot_speed += 10
        elif self.stat == SHOOT_DELAY:
            player.weapon.reduce_fire_rate()
        elif self.stat == MAX_HP:
            player.max_HP += 5
        elif self.stat == MIN_DELAY:
            player.weapon.reduce_min_fire_rate()
        screen = main_game.get_screen()
        screen.print_text(stat_text_table[self.stat])
        main_game.add_delete_list(self)

    def update(self):
        self.dir += self.speed * framework.frame_time
        pass

    def draw(self, screen):
        self.image.rotate_draw(self.dir, self.x - screen.x, self.y - screen.y, self.size, self.size)


