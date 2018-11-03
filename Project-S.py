from pico2d import *
import framework
import main_game
import main_menu
import test

open_canvas(framework.GAME_SIZE[0], framework.GAME_SIZE[1], sync=True)





#main
#framework.run(main_game)
framework.run(main_menu)

close_canvas()



