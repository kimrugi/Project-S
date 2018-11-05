from pico2d import *
import framework
import main_game
import main_menu
import test

open_canvas(framework.WINDOW_SIZE[0], framework.WINDOW_SIZE[1], sync=True)





#main
framework.run(main_game)
#framework.run(main_menu)

close_canvas()



