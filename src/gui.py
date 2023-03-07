import curses

from src import consts
from src import player


class Gui:
    def __init__(self) -> None:
        self.scr = curses.initscr()
        self.wind = curses.newwin(consts.WIND_HGT, consts.WIND_WDT, 2, 2)

        self.wind.keypad(1)
        curses.curs_set(0)

    def getChar(self):
        return self.wind.getch()

    def update(self, user: player):
        self.wind.clear()
        self.wind.border(0)
        self.wind.addch(user.y, user.x, user.icon)
        self.wind.refresh()

    def close():
        curses.endwin()
