from pico2d import *
import main_game
class SpaceStation():
    image = None
    font = None
    def load_image(self):
        if SpaceStation.image is None:
            SpaceStation.image = load_image('resources\\etc\\Spacestation.png')

    def __init__(self):
        self.load_image()
        if SpaceStation.font is None:
            SpaceStation.font = load_font('resources\\text\\kongtext.ttf')
        self.resource_amount = 0
        self.boss_counter = 0
        self.x, self.y = 4200, 4200
        self.size = 200
        pass

    def update(self):
        pass

    def get_resource(self):
        player = main_game.get_player()
        self.resource_amount += player.carrying_resource
        self.boss_counter += player.carrying_resource
        player.carrying_resource = 0
        player.HP = player.max_HP
        if self.resource_amount > 30:
            self.resource_amount -= 30
            main_game.add_upgrade(self.x, self.y)
        if self.boss_counter > 1000:
            main_game.spawner.spawn_boss()

    def get_bb(self):
        return self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size

    def draw(self, screen):
        x, y = self.x - screen.x, self.y - screen.y
        self.image.draw(x, y, self.size, self.size)
        self.font.draw(x - 80, y + 120, "%5d" % self.resource_amount, (255, 255, 255))
