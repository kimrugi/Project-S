
from pico2d import *
import framework

image_x, image_y = 192, 512
class test_class:
    def __init__(self):
        self.image = load_image('resources\\character\\shipsprite1.png')
        self.x, self.y = 500, 500
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(0, 0, image_x // 3, image_y // 8, self.x, self.y)

def enter():
    pass


def exit():
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
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
               framework.quit()


def update():
    pass


def draw():

   pass


