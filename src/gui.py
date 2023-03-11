import curses

import time

from src import consts
from src import player
from src import invader


class Gui:
    def __init__(self) -> None:
        self.scr = curses.initscr()
        self.wind = curses.newwin(consts.WIND_HGT, consts.WIND_WDT, 2, 2)

        self.wind.keypad(1)
        curses.curs_set(0)

    def getChar(self) -> int:
        return self.wind.getch()

    def delChar(self, pos_y, pos_x) -> None:
        self.wind.delch(pos_y, pos_x)

    def draw_player(self, user: player) -> None:
        self.wind.addch(user.y, user.x, user.icon)

    def erase_player(self, user: player) -> None:
        self.wind.addch(user.y, user.x, " ")

    def move_player(self, user: player, key: int) -> None:
        self.erase_player(user)
        user.update_loc(key)
        self.draw_player(user)

    def player_thread(self, user: player) -> None:
        while True:
            key = self.getChar()
            self.move_player(user, key)
            self.wind.refresh()

    def draw_invader(self, alien: invader) -> None:
        self.wind.addch(alien.y, alien.x, alien.icon)

    def erase_invader(self, alien: invader) -> None:
        self.wind.addch(alien.y, alien.x, " ")

    def move_invader(self, alien: invader) -> None:
        while alien.y < consts.PLAYER_Y - consts.STEP:
            for _ in range(consts.GAME_MARGIN_X, consts.GAME_WDT - consts.STEP + 1):
                self.erase_invader(alien)
                alien.move_right()
                self.draw_invader(alien)
                self.wind.refresh()
                time.sleep(0.1)

            self.erase_invader(alien)
            alien.move_down()
            self.draw_invader(alien)
            self.wind.refresh()
            time.sleep(0.1)

            for _ in range(consts.GAME_WDT - consts.STEP, consts.GAME_MARGIN_X - 1, -1):
                self.erase_invader(alien)
                alien.move_left()
                self.draw_invader(alien)
                self.wind.refresh()
                time.sleep(0.1)

            self.erase_invader(alien)
            alien.move_down()
            self.draw_invader(alien)
            self.wind.refresh()
            time.sleep(0.1)

    def invader_thread(self, alien: invader) -> None:
        self.move_invader(alien)

    def close(self):
        curses.endwin()
