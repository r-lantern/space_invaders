import curses

from src import consts


class Player:
    def __init__(self) -> None:
        self.icon = "^"

        self.x = consts.GAME_MARGIN_X
        self.y = consts.PLAYER_Y

    def move(self, key: int) -> None:
        if key == curses.KEY_LEFT and self.x >= consts.GAME_MARGIN_X + consts.STEP:
            self.x -= consts.STEP
        elif key == curses.KEY_RIGHT and self.x <= consts.GAME_WDT - consts.STEP:
            self.x += consts.STEP
