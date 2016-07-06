import curses_window
import time

w = curses_window.CursesWindow()
w.add_pane('pane1', (0, 0), (32, 8))
w.add_pane('pane2', (32, 0), (32, 8))
w.draw()
w.getch()
w.close()
