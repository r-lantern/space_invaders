import curses

import time

from src import consts
from src import player
from src import invader


class Gui:
    def __init__(self, user: player, alien: invader) -> None:
        self.scr = curses.initscr()
        self.wind = curses.newwin(consts.WIND_HGT, consts.WIND_WDT, 2, 2)

        self.player = user
        self.invader = alien

        self.wind.keypad(1)
        curses.curs_set(0)

    def getChar(self) -> int:
        return self.wind.getch()

    def draw_player(self) -> None:
        self.wind.addch(self.player.y, self.player.x, self.player.icon)

    def move_player(self, key: int) -> None:
        self.player.update_loc(key)

    def player_thread(self) -> None:
        while True:
            key = self.getChar()
            self.move_player(self.player, key)
            self.draw(self.player)

    def move_invader(self) -> None:
        while self.invader.y < consts.PLAYER_Y - consts.STEP:
            for _ in range(consts.GAME_MARGIN_X, consts.GAME_WDT - consts.STEP + 1):
                self.invader.move_right()
                self.draw()
                time.sleep(0.1)

            self.invader.move_down()
            self.draw()
            time.sleep(0.1)

            for _ in range(consts.GAME_WDT - consts.STEP, consts.GAME_MARGIN_X - 1, -1):
                self.invader.move_left()
                self.draw()
                time.sleep(0.1)

            self.invader.move_down()
            self.draw()
            time.sleep(0.1)

    def draw_invader(self) -> None:
        self.wind.addch(self.invader.y, self.invader.x, self.invader.icon)

    def draw(self) -> None:
        self.wind.clear()
        self.wind.border(0)
        self.draw_player()
        self.draw_invader()
        self.wind.refresh()

    def close(self):
        curses.endwin()
