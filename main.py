import curses
from curses import KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT


LINES = 10
COLUMNS = 20


class Star:
    """ Star object you can move around in the window (x=down,up|lines, y=left,right|columns)"""

    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.window = window

    def render(self):
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)

    def move_left(self):
        if self.y - 1 <= 0:
            return
        self.window.addch(self.x, self.y, ' ')
        self.y = self.y - 1
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)

    def move_right(self):
        if self.y + 2 >= COLUMNS:
            return
        self.window.addch(self.x, self.y, ' ')
        self.y = self.y + 1
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)

    def move_up(self):
        if self.x - 1 <= 0:
            return
        self.window.addch(self.x, self.y, ' ')
        self.x = self.x - 1
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)

    def move_down(self):
        if self.x + 2 >= LINES:
            return
        self.window.addch(self.x, self.y, ' ')
        self.x = self.x + 1
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)


def main2():
    screen = curses.initscr()
    h, w = screen.getmaxyx()
    window = curses.newwin(LINES, COLUMNS, 0, 0)

    window.keypad(1)
    curses.curs_set(0)

    star = Star(2, 10, window)
    star.render()

    while True:
        window.border(0)
        window.timeout(100)

        key = window.getch()

        if key == -1:
            continue

        # 0-Left, 1-Right, 3-Up, 2-Down
        if key == KEY_LEFT:
            star.move_left()
        elif key == KEY_RIGHT:
            star.move_right()
        elif key == KEY_UP:
            star.move_up()
        elif key == KEY_DOWN:
            star.move_down()
        else:
            pass


if __name__ == '__main__':
    main2()
