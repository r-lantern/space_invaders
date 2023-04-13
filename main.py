from src.gui import Gui
from src.invaders import Invaders
from src.player import Player

import src.consts as consts

import curses
import time


player = Player()
invaders = Invaders(15)
game = Gui(player, invaders)

game.draw_message("PRESS ANY KEY")
game.key_to_continue()

game.draw()
dir = consts.DIR_RIGHT

while True:
    key = game.get_char()

    if key == curses.KEY_RIGHT:
        player.move_right()
    elif key == curses.KEY_LEFT:
        player.move_left()

    if dir == consts.DIR_RIGHT:
        if not invaders.move_right():
            dir = consts.DIR_DOWN1

    elif dir == consts.DIR_DOWN1:
        if invaders.move_down():
            dir = consts.DIR_LEFT
        else:
            break

    elif dir == consts.DIR_LEFT:
        if not invaders.move_left():
            dir = consts.DIR_DOWN2

    elif dir == consts.DIR_DOWN2:
        if invaders.move_down():
            dir = consts.DIR_RIGHT
        else:
            break

    game.draw()
    time.sleep(consts.DELAY)

game.draw_message("GAME OVER")
time.sleep(3)
game.key_to_continue()
game.close()
