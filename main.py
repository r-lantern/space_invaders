import src.player as player
import src.gui as gui

gui = gui.Gui()
player = player.Player()

gui.update(player)

while True:
    key = gui.getChar()
    player.update_loc(key)
    gui.update(player)
