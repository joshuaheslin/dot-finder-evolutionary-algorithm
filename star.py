import curses
from config import COLUMNS, LINES


class Star:
    """
        Star object you can move around in the window (x=down,up|lines, y=left,right|columns)
    """

    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.window = window

    def render(self):
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)

    @property
    def position(self):
        return (self.x, self.y)

    def get_score(self, target):
        a_factor = abs(self.x - target[0])
        b_factor = abs(self.y - target[1])
        return a_factor + b_factor

    def move_left(self):
        if self.y - 1 <= 0:
            return
        self.window.addch(self.x, self.y, ' ')
        self.y -= 1
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)

    def move_right(self):
        if self.y + 2 >= COLUMNS:
            return
        self.window.addch(self.x, self.y, ' ')
        self.y += 1
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)

    def move_up(self):
        if self.x - 1 <= 3:
            return
        self.window.addch(self.x, self.y, ' ')
        self.x -= 1
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)

    def move_down(self):
        if self.x + 2 >= LINES:
            return
        self.window.addch(self.x, self.y, ' ')
        self.x += 1
        self.window.addch(self.x, self.y, curses.ACS_DIAMOND)
