import src.consts as consts
import src.player as player
import src.gui as gui
import src.invaders as invaders

import curses
import time


user = player.Player()
aliens = invaders.Invaders(15)
game = gui.Gui(user, aliens)

game.draw_message("SPACE INVADERS")
game.wind.nodelay(False)
game.get_char()

game.wind.nodelay(True)
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
        else:
            break

    elif dir == consts.DIR_LEFT:
        if not aliens.move_left():
            dir = consts.DIR_DOWN2

    elif dir == consts.DIR_DOWN2:
        if aliens.move_down():
            dir = consts.DIR_RIGHT
        else:
            break

    game.draw()
    time.sleep(consts.DELAY)

game.draw_message("GAME OVER")
game.wind.nodelay(False)
game.get_char()
