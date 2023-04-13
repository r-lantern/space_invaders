import curses

from src import consts
from src.player import Player
from src.invader import Invader
from src.invaders import Invaders


class Gui:
    def __init__(self, player: Player, invaders: Invaders) -> None:
        self.scr = curses.initscr()
        self.wind = curses.newwin(consts.WIND_HGT, consts.WIND_WDT, 2, 2)
        self.wind.keypad(1)
        curses.curs_set(0)

        self.player = player
        self.invaders = invaders

    def get_char(self) -> int:
        return self.wind.getch()

    def key_to_continue(self) -> None:
        self.wind.nodelay(False)
        self.get_char()
        self.wind.nodelay(True)

    def draw_player(self) -> None:
        self.wind.addch(self.player.y, self.player.x, self.player.icon)

    def draw_invader(self, invader: Invader) -> None:
        self.wind.addch(invader.y, invader.x, invader.icon)

    def draw_invaders(self) -> None:
        for invader in self.invaders.invader_set:
            self.draw_invader(invader)

    def draw(self) -> None:
        self.wind.clear()
        self.wind.border(0)
        self.draw_player()
        self.draw_invaders()
        self.wind.refresh()

    def draw_message(self, msg: str) -> None:
        self.wind.clear()
        self.wind.border(0)
        self.wind.addstr(
            consts.WIND_HGT // 2,
            consts.WIND_WDT // 2 - len(msg) // 2,
            msg,
        )
        self.wind.refresh()

    def close(self):
        curses.endwin()
