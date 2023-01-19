import curses
from curses import KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT

from star import Star
from config import COLUMNS, LINES


def main():
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
    main()
