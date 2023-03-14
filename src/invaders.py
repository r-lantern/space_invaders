import random

from src import consts
from src import invader


class Invaders:
    def __init__(self, num_invaders: int) -> None:
        self.size_x = consts.GAME_WDT // 2
        self.size_y = 3

        self.offset_x = consts.GAME_MARGIN_X + self.size_x // 2
        self.offset_y = consts.GAME_MARGIN_Y + 1

        self.num_invaders = num_invaders
        self.invader_set = set()
        self.locations = set()
        self.set_invaders()

        self.left_most = consts.WIND_WDT + 1
        self.right_most = -1
        self.lowest = -1

        self.set_left_most()
        self.set_right_most()
        self.set_lowest()
        print(self.locations)
        print(self.left_most, self.right_most, self.lowest)

    def set_invaders(self) -> None:
        num = 0
        while num < self.num_invaders:
            rand_x = random.randint(0, self.size_x - 1)
            rand_y = random.randint(0, self.size_y - 1)
            loc_x = rand_x + self.offset_x
            loc_y = rand_y + self.offset_y
            if (loc_x, loc_y) not in self.locations:
                self.locations.add((loc_x, loc_y))
                self.invader_set.add(invader.Invader(loc_x, loc_y))
                num += 1

    def set_left_most(self) -> None:
        for loc in self.locations:
            if loc[0] < self.left_most:
                self.left_most = loc[0]

    def set_right_most(self) -> None:
        for loc in self.locations:
            if loc[0] > self.right_most:
                self.right_most = loc[0]

    def set_lowest(self) -> None:
        for loc in self.locations:
            if loc[1] > self.lowest:
                self.lowest = loc[1]

    def move_left(self) -> bool:
        if self.left_most < consts.GAME_MARGIN_X + consts.STEP:
            return False

        for alien in self.invader_set:
            alien.move_left()

        set_copy = self.locations.copy()
        for pos in set_copy:
            self.locations.add((pos[0] - consts.STEP, pos[1]))
            self.locations.remove(pos)

        self.left_most -= 1
        self.right_most -= 1
        return True

    def move_right(self) -> bool:
        if self.right_most > consts.GAME_WDT - consts.STEP:
            return False

        for alien in self.invader_set:
            alien.move_right()

        set_copy = self.locations.copy()
        for pos in set_copy:
            self.locations.add((pos[0] + consts.STEP, pos[1]))
            self.locations.remove(pos)

        self.left_most += 1
        self.right_most += 1
        return True

    def move_down(self) -> bool:
        if self.lowest >= consts.PLAYER_Y - 1:
            return False

        for alien in self.invader_set:
            alien.move_down()

        set_copy = self.locations.copy()
        for pos in set_copy:
            self.locations.add((pos[0], pos[1] + consts.STEP))
            self.locations.remove(pos)

        self.lowest += 1
        return True
