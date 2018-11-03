from pico2d import *
WIDTH, HEIGHT = 1280, 720

open_canvas(WIDTH, HEIGHT, sync=True)

import framework
import main_game
import test



#main
framework.run(main_game)


close_canvas()



