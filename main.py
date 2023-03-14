import src.player as player
import src.gui as gui
import src.invaders as invaders


user = player.Player()
aliens = invaders.Invaders(10)
game = gui.Gui(user, aliens)

game.draw()
game.move_invaders()
