import curses

scr = curses.initscr()
hgt, wdt = scr.getmaxyx()
wind = curses.newwin(hgt, wdt, 0, 0)

curses.endwin()
