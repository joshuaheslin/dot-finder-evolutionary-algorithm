import curses
import sys
from curses.textpad import Textbox, rectangle
from curses import wrapper
from curses import KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT


class StdOutWrapper:
    """ Helper to print on terminal """
    text = ""

    def write(self, txt):
        self.text += txt
        self.text += "\n"

    def get_text(self):
        return self.text


def main():
    mystdout = StdOutWrapper()
    sys.stdout = mystdout
    sys.stderr = mystdout

    curses.initscr()
    curses.beep()
    curses.beep()
    window = curses.newwin(10, 10, 0, 0)
    window.timeout(60)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    window.addstr(5, 12, 'Adding this text to row 5, column 12')
    # window.refresh()

    while True:
        c = window.getch()
        if c == ord('p'):
            window.addstr(c)
        elif c == ord('q'):
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0

    return
    # userInput = stdscr.getKey()

    while True:
        window.clear()
        window.border(0)

        # rendering the objects
        # snake.render()
        # food.render()

        # window.addstr(0, 5, snake.getScore)
        event = window.getch()

        print(event)

        if event == 27:
            break

        # if snake.head.x == food.x and snake.head.y == food.y:
        #     snake.eatFood(food)
        #     curses.beep()

        # event = astar.getKey(food, snake)
        # print(event)

        if event in (KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT):
            pass
            # snake.makeMove(event)

            # snake.update()
            # if snake.collided():
            #     break

    curses.endwin()
    print(f"High score :: {1}")

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    sys.stdout.write(mystdout.get_text())

    return
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    editwin = curses.newwin(5, 30, 2, 1)
    rectangle(stdscr, 1, 0, 1+5+1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()

    while True:
        c = stdscr.getch()
        if c == ord('p'):
            print(c)
        elif c == ord('q'):
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0


LINES = 10
COLUMNS = 20


def main2():
    screen = curses.initscr()
    h, w = screen.getmaxyx()
    window = curses.newwin(LINES, COLUMNS, 0, 0)

    window.keypad(1)
    curses.curs_set(0)

    star_position = [2, 10]

    window.addch(star_position[0], star_position[1], curses.ACS_DIAMOND)

    while True:
        window.clear()
        window.border(0)
        window.timeout(100)

        key = window.getch()

        if key == -1:
            continue
        if key in (curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN):

            if star_position[0] - 1 <= 0 or star_position[1] - 1 <= 0:
                continue

            # 0-Left, 1-Right, 3-Up, 2-Down
            if key == curses.KEY_LEFT:
                window.addch(star_position[0], star_position[1], ' ')
                star_position = [star_position[0], star_position[1] - 1]
                window.addch(star_position[0],
                             star_position[1], curses.ACS_DIAMOND)
            elif key == curses.KEY_RIGHT:
                window.addch(star_position[0], star_position[1], ' ')
                star_position = [star_position[0], star_position[1] + 1]
                window.addch(star_position[0],
                             star_position[1], curses.ACS_DIAMOND)
            elif key == curses.KEY_UP:
                window.addch(star_position[0], star_position[1], ' ')
                star_position = [star_position[0] - 1, star_position[1]]
                window.addch(star_position[0],
                             star_position[1], curses.ACS_DIAMOND)
            elif key == curses.KEY_DOWN:
                window.addch(star_position[0], star_position[1], ' ')
                star_position = [star_position[0] + 1, star_position[1]]
                window.addch(star_position[0],
                             star_position[1], curses.ACS_DIAMOND)
            else:
                pass

            # key = -1
            prev_button_direction = button_direction
            # sc.addstr(10, 30, 'Your Score is:  '+str(score))
            # sc.refresh()
            # time.sleep(2)
            curses.endwin()
            # print(a)
            # print(10, 20)
            window.refresh()


if __name__ == '__main__':
    main2()
