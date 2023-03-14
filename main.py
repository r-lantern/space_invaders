import src.player as player
import src.gui as gui
import src.invaders as invaders

import curses


user = player.Player()
aliens = invaders.Invaders(10)
game = gui.Gui(user, aliens)

game.draw()

while True:
    key = game.get_char()

    if key == curses.KEY_RIGHT:
        user.move_right()
    elif key == curses.KEY_LEFT:
        user.move_left()

    game.draw()
