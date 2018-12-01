from pico2d import *
import default_enemy
import random
import main_game
import framework
SIZE_X, SIZE_Y = 8400, 8400

LEFT, RIGHT = 4200 - 500, 4200 + 500
TOP, BOTTOM = 4200 - 300, 4200 + 300


class Asteroid(default_enemy.DefaultEnemy):
    image = None
    def load_image(self):
        if Asteroid.image is None:
            Asteroid.image = load_image('resources\\etc\\aster.png')

    def reset_status(self):
        self.max_HP = random.randint(10, 100)
        self.HP = self.max_HP
        self.size = self.max_HP
        x,y = random.randint(0, SIZE_X), random.randint(0, SIZE_Y)
        while(LEFT <  x < RIGHT and TOP < y < BOTTOM):
            x,y = random.randint(0, SIZE_X), random.randint(0, SIZE_Y)
        self.x = random.randint(0, SIZE_X)
        self.y = random.randint(0, SIZE_Y)
        self.dir = (random.randint(0, 1000) - 500) / 500
        self.size_propotion = 1
        self.speed = 10 / self.size

    def build_behavior_tree(self):
        self.bt = None

    def get_damaged(self, damage):
        self.HP -= damage
        self.hp_bar.change_hp()
        if self.HP < 0:
            player = main_game.get_player()
            player.give_resource(self.max_HP)
            main_game.add_delete_list(self)
            pass

    def update(self):
        self.dir += self.speed * framework.frame_time
        pass

    def draw(self, screen):
        self.image.rotate_draw(self.dir, self.x - screen.x, self.y - screen.y, self.size, self.size)
        if self.HP < self.max_HP:
            self.hp_bar.draw(screen)


