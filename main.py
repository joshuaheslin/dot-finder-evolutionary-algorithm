import curses
import random
from curses import KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT

from star import Star
from config import COLUMNS, LINES

target = [5, 5]
inputs = [260, 258, 261, 259]
# inputs = [KEY_LEFT, KEY_DOWN, KEY_RIGHT, KEY_UP, -1]


def run_game(instructions, manual_mode=False):
    window.keypad(1)
    curses.curs_set(0)

    star = Star(6, 10, window)
    star.render()

    while True:
        window.border(0)
        window.timeout(100)
        window.addstr(0, 0, f'Position: {star.position}')
        window.addstr(9, 0, f'Target: {target}')
        window.addch(target[0], target[1], curses.ACS_BLOCK)

        if len(instructions) == 0:
            return star

        key = None
        if manual_mode:
            key = window.getch()
        else:
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
    best_score = 1000
    best_instructions = [random.choice(inputs) for _ in range(20)]
    current_game_score = 1000
    generation_counter = 0

    while best_score >= 2:
        results = []

        for _ in range(5):
            best_instructions[12] = random.choice(inputs)
            best_instructions[15] = random.choice(inputs)
            best_instructions[17] = random.choice(inputs)
            best_instructions[18] = random.choice(inputs)
            best_instructions[19] = random.choice(inputs)

            instructions = best_instructions.copy()
            saved_instructions = instructions.copy()

            game_star = run_game(instructions)
            current_game_score = game_star.get_score(target)

            results.append((current_game_score, saved_instructions))

        best_results = sorted(results, key=lambda tup: tup[0])

        current_best_score = best_results[0][0]
        if current_best_score < best_score:
            best_score = current_best_score
            best_instructions = best_results[0][1]
        generation_counter += 1

        window.addstr(1, 1, f"Best: {best_score}")
        window.addstr(2, 1, f"Gen: {generation_counter}")

    return [best_score, best_instructions]


if __name__ == '__main__':
    screen = curses.initscr()
    h, w = screen.getmaxyx()
    window = curses.newwin(LINES, COLUMNS, 0, 0)

    optimised_result = main()
    print(optimised_result)

    # instructions = [261, 258, 258, 258, 258, 260, 258, 260, 260,
    #                 260, 259, 259, 259, 261, 258, 259, 260, 260, 260, 259]
    # run_game(instructions, manual_mode=False)
