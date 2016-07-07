import curses

class CursesPane:
    __pane = None
    __x = 0
    __y = 0
    __width = 0
    __height = 0
    __title = ''

    def __init__(self, pos, size, title = ''):
        self.__x = pos[0]
        self.__y = pos[1]
        self.__width = size[0]
        self.__height = size[1]
        self.__title = title
        self.__pane = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    def close(self):
        del(self.__pane)

    @property
    def pane(self):
        return self.__pane

    @property
    def x(self):
        return self.__x    

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def title(self):
        return self.__title

    def draw(self):
        self.__draw_border()
        self.__draw_title()
        self.pane.refresh()

    def __draw_border(self):
        self.pane.box()

    def __draw_title(self):
        if len(self.title) > 0:
            dims = self.pane.getmaxyx()
            self.pane.addstr(0, int(dims[1] / 2) - int(len(self.title) / 2) - int(len(self.title) % 2), self.title)

