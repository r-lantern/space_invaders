import random

from src import consts
from src import invader


class Invaders:
    def __init__(self, num_invaders: int) -> None:
        self.size_x = consts.GAME_WDT - 6
        self.size_y = 3

        self.offset_x = consts.GAME_MARGIN_X + 3
        self.offset_y = consts.GAME_MARGIN_Y + 1

        self.num_invaders = num_invaders
        self.array = [[None for _ in range(self.size_x)] for _ in range(self.size_y)]
        self.create_array()

    def create_array(self) -> None:
        invaders_x = [
            random.randint(0, self.size_x - 1) for _ in range(self.num_invaders)
        ]
        invaders_y = [
            random.randint(0, self.size_y - 1) for _ in range(self.num_invaders)
        ]

        for num in range(0, self.num_invaders):
            loc_x = invaders_x[num]
            loc_y = invaders_y[num]
            self.array[loc_y][loc_x] = invader.Invader(
                invaders_x[num] + self.offset_x, invaders_y[num] + self.offset_y
            )

    def move_left(self) -> bool:
        for col in range(0, self.size_x):
            for row in range(0, self.size_y):
                if self.array[row][col]:
                    if not self.array[row][col].move_left():
                        return False
        return True

    def move_right(self) -> bool:
        for col in range(self.size_x - 1, 0 - 1, -1):
            for row in range(0, self.size_y):
                if self.array[row][col]:
                    if not self.array[row][col].move_right():
                        return False
        return True

    def move_down(self) -> bool:
        for row in range(self.size_y - 1, 0 - 1, -1):
            for col in range(0, self.size_x, 1):
                if self.array[row][col]:
                    if not self.array[row][col].move_down():
                        return False
        return True
