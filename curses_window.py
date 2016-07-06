import curses
from curses_pane import CursesPane

class CursesWindow:
    __screen = None
    __panes = dict()

    def __init__(self):
        self.__screen = curses.initscr()
        curses.start_color()
        curses.noecho()
        self.__screen.clear()

    @property
    def screen(self):
        return self.__screen

    @property
    def panes(self):
        return self.__panes

    def size(self):
        dims = self.__screen.getmaxyx()
        return dims[1], dims[0]

    def close(self):
        curses.endwin()

    def add_pane(self, name, pos, size):
        pane = CursesPane(self.__screen, pos, size)
        self.__panes[name] = pane

    def remove_pane(self, name):
        del(self.panes[name])

    def draw(self):
        for pane in self.panes.values():
            pane.draw()

        self.screen.refresh()

    def getch(self):
        return self.screen.getch()
