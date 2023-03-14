from src import consts


class Player:
    def __init__(self) -> None:
        self.icon = "^"

        self.x = consts.GAME_WDT // 2
        self.y = consts.PLAYER_Y

    def move_right(self) -> None:
        if self.x <= consts.GAME_WDT - consts.STEP:
            self.x += consts.STEP

    def move_left(self) -> None:
        if self.x >= consts.GAME_MARGIN_X + consts.STEP:
            self.x -= consts.STEP
