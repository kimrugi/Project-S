from pico2d import *
import math
import main_game
import framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import bullet
import game_world
import default_enemy
import nokkey
import random
PIXEL_PER_KILOMETER = 5
QUAD_PI = math.pi / 4
HALF_OF_QUAD_PI = QUAD_PI / 2

LEFT, UP, RIGHT, BOTTOM = 0, 44, 90, 3
IMAGE_WIDTH, IMAGE_HEIGHT = 90, 41
WINDOW_SIZE = (960, 540)
MIDDLE = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

class Flatter(default_enemy.DefaultEnemy):

    def reset_status(self):
        self.set_speed(10)
        self.shoot_delay = 0.3
        self.max_HP = 300
        self.size = 100
        self.HP = 300
        self.damage_amount = 10
        pass

    def attack(self):
        if self.shoot_count > self.shoot_delay:
            self.shoot_count -= self.shoot_delay
            self.random_shoot()

    def find_player(self):
        screen = main_game.get_screen()
        x, y = screen.x + MIDDLE[0], screen.y + MIDDLE[1] + 200
        self.dir = math.atan2(x - self.x, y - self.y)
        return BehaviorTree.SUCCESS

    def get_damaged(self, damage):
        self.HP -= damage
        self.hp_bar.change_hp()
        if self.HP < 0:
            main_game.spawner.del_boss()
            main_game.add_delete_list(self)
            pass

    def random_shoot(self):
        ran_x = random.randint(-1000, 1000) / 1000
        main_game.add_bullet(self.x, self.y, ran_x, -1, self, 200, self.damage_amount)

        pass

    def spawn_nokkeys(self):
        nok = nokkey.Nokkey(self.x - IMAGE_HEIGHT / 2, self.y - IMAGE_HEIGHT / 2)
        game_world.add_object(nok, 1)
        main_game.add_enemys(nok)
        pass

    def draw(self, screen):
        Flatter.image.clip_draw(LEFT, BOTTOM, IMAGE_WIDTH, IMAGE_HEIGHT, self.x - screen.x, self.y - screen.y,
                                     self.size * 2, self.size)
        if self.HP < self.max_HP:
            self.hp_bar.draw(screen)


    pass
