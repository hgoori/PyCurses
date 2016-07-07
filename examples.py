import curses
import curses_window
import time

screen = curses.initscr()
curses.start_color()
curses.noecho()

try:
    w = curses_window.CursesWindow(screen)
    w.add_pane('pane1', (0, 0), (32, 8), 'This is a pane1')
    w.add_pane('pane2', (33, 0), (32, 8), 'This is a pane2')
    w.draw()
    w.getch()
finally:
    curses.endwin()
