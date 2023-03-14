import src.consts as consts
import src.player as player
import src.gui as gui
import src.invaders as invaders

import curses
import time


user = player.Player()
aliens = invaders.Invaders(2)
game = gui.Gui(user, aliens)

game.draw()
dir = consts.DIR_RIGHT

while True:
    key = game.get_char()

    if key == curses.KEY_RIGHT:
        user.move_right()
    elif key == curses.KEY_LEFT:
        user.move_left()

    if dir == consts.DIR_RIGHT:
        if not aliens.move_right():
            dir = consts.DIR_DOWN1

    elif dir == consts.DIR_DOWN1:
        if aliens.move_down():
            dir = consts.DIR_LEFT

    elif dir == consts.DIR_LEFT:
        if not aliens.move_left():
            dir = consts.DIR_DOWN2

    elif dir == consts.DIR_DOWN2:
        if aliens.move_down():
            dir = consts.DIR_RIGHT

    game.draw()
    time.sleep(consts.DELAY)
