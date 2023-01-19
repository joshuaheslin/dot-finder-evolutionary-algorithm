import curses
import sys
import random
import time
from curses import KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT

from star import Star
from config import COLUMNS, LINES

# 260 258 261 259
inputs = [KEY_LEFT, KEY_DOWN, KEY_RIGHT, KEY_UP]


def run_game(instructions):
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
        window.addstr(9, 0, f'Position: {star.position}')

        if len(instructions) == 0:
            return star

        key = instructions.pop()
        key_1 = window.getch()

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


def main():
    instructions = [random.choice(inputs) for _ in range(10)]
    game_star = run_game(instructions)
    target = [5, 5]
    print("\n")
    print(f"Final position: {game_star.position}")
    print(f"Final score: {game_star.get_score(target)}")


if __name__ == '__main__':
    main()
