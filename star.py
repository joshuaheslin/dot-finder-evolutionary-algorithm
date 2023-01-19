from curses import KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT
from random import randint

from constants import *


class Star(object):
    """ Food with random location """

    def __init__(self, window, snake, char=FOOD_CHAR):
        self.x = randint(10, MAX_X)
        self.y = randint(10, MAX_Y)
        self.char = char
        self.window = window
        self.snake = snake

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def reset(self):
        self.x = randint(10, MAX_X)
        self.y = randint(10, MAX_Y)

        if self.collides():
            self.reset()

    def collides(self):
        return any([body.position == (self.x, self.y) for body in self.snake.body[: -1]])
