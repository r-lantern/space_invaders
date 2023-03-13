import src.player as player
import src.gui as gui
import src.invader as invader
import src.consts as consts


user = player.Player()
alien = invader.Invader(consts.GAME_MARGIN_X, consts.GAME_MARGIN_Y)
game = gui.Gui(user, alien)
