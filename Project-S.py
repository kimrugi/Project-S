from pico2d import *
import framework
import game_value
import main_game
import main_menu
import test

open_canvas(game_value.WINDOW_SIZE[0], game_value.WINDOW_SIZE[1], sync=True)

framework.run(main_menu)

close_canvas()



