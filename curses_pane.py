import curses

class CursesPane:
    __screen = None
    __x = 0
    __y = 0
    __width = 0
    __height = 0

    def __init__(self, screen, pos, size):
        self.__screen = screen
        self.__x = pos[0]
        self.__y = pos[1]
        self.__width = size[0]
        self.__height = size[1]

    @property
    def screen(self):
        return self.__screen

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

    def draw(self):
        self.__draw_outline()

    def __draw_outline(self):
        for x in range(self.x, self.x + self.width + 1):
            self.screen.addstr(self.y, x, '-')
            self.screen.addstr(self.y + self.height, x, '-')

        for y in range(self.y, self.y + self.height + 1):
            self.screen.addstr(y, self.x, '|')
            self.screen.addstr(y, self.x + self.width, '|')

