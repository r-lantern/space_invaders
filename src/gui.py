import curses

from src import consts
from src import player
from src import invader
from src import invaders


class Gui:
    def __init__(self, user: player, aliens: invaders) -> None:
        self.scr = curses.initscr()
        self.wind = curses.newwin(consts.WIND_HGT, consts.WIND_WDT, 2, 2)
        self.wind.nodelay(True)
        self.wind.keypad(1)
        curses.curs_set(0)

        self.player = user
        self.invaders = aliens

    def get_char(self) -> int:
        return self.wind.getch()

    def draw_player(self) -> None:
        self.wind.addch(self.player.y, self.player.x, self.player.icon)

    def draw_invader(self, invader: invader) -> None:
        self.wind.addch(invader.y, invader.x, invader.icon)

    def draw_invaders(self) -> None:
        for alien in self.invaders.invader_set:
            self.draw_invader(alien)

    def draw(self) -> None:
        self.wind.clear()
        self.wind.border(0)
        self.draw_player()
        self.draw_invaders()
        self.wind.refresh()

    def close(self):
        curses.endwin()
