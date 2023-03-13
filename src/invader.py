from src import consts


class Invader:
    def __init__(self, loc_x: int, loc_y: int) -> None:
        self.icon = "@"

        self.x = loc_x
        self.y = loc_y

    def move_left(self) -> bool:
        if self.x < consts.GAME_MARGIN_X + consts.STEP:
            return False
        self.x -= consts.STEP
        return True

    def move_right(self) -> bool:
        if self.x > consts.GAME_WDT - consts.STEP:
            return False
        self.x += consts.STEP
        return True

    def move_down(self) -> bool:
        if self.y >= consts.PLAYER_Y:
            return False
        self.y += consts.STEP
        return True
