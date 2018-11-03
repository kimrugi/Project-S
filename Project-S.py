from pico2d import *
WIDTH, HEIGHT = 1280, 720

open_canvas(WIDTH, HEIGHT, sync=True)

import framework
import main_game
import main_menu
import test



#main
#framework.run(main_game)
framework.run(main_menu)

close_canvas()



