import curses

import time

from src import consts
from src import player
from src import invader
from src import invaders


class Gui:
    def __init__(self, user: player, aliens: invaders) -> None:
        self.scr = curses.initscr()
        self.wind = curses.newwin(consts.WIND_HGT, consts.WIND_WDT, 2, 2)

        self.player = user
        self.invaders = aliens

        self.wind.keypad(1)
        curses.curs_set(0)

    def getChar(self) -> int:
        return self.wind.getch()

    def draw_player(self) -> None:
        self.wind.addch(self.player.y, self.player.x, self.player.icon)

    def move_player(self, key: int) -> None:
        self.player.move(key)

    def player_thread(self) -> None:
        while True:
            key = self.getChar()
            self.move_player(key)

    def draw_invader(self, invader: invader) -> None:
        self.wind.addch(invader.y, invader.x, invader.icon)

    def draw_invaders(self) -> None:
        size_x = len(self.invaders.array[0])
        size_y = len(self.invaders.array)

        for row in range(0, size_y):
            for col in range(0, size_x):
                alien = self.invaders.array[row][col]
                if alien:
                    self.draw_invader(alien)

    def move_invaders(self) -> None:
        while True:
            while self.invaders.move_right():
                self.draw()
            if not self.invaders.move_down():
                return
            self.draw()
            while self.invaders.move_left():
                self.draw()
            if not self.invaders.move_down():
                return
            self.draw()

    def draw(self) -> None:
        self.wind.clear()
        self.wind.border(0)
        self.draw_player()
        self.draw_invaders()
        self.wind.refresh()
        time.sleep(0.5)

    def close(self):
        curses.endwin()
