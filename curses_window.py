import curses
from curses_pane import CursesPane

class CursesWindow:
    __screen = None
    __panes = dict()

    def __init__(self, screen):
        self.__screen = curses.initscr()
        self.__screen.clear()

    @property
    def screen(self):
        return self.__screen

    @property
    def panes(self):
        return self.__panes

    def size(self):
        dims = self.screen.getmaxyx()
        return dims[1], dims[0]

    def add_pane(self, id, pos, size, title = ''):
        pane = CursesPane(pos, size, title)
        self.panes[id] = pane

    def remove_pane(self, id):
        pane = self.panes[id]
        if pane is not None:
            pane.close()
            del(self.panes[id])

    def draw(self):
        self.screen.clear()
        self.screen.refresh()

        for pane in self.panes.values():
            pane.draw()

    def getch(self):
        return self.screen.getch()
