# This file contains all functions which are related to user interaction via keyboard

import sudoku_logic as logic

class _Getch:                   # goes to a file user input
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix: # goes to a file user input
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:         # goes to a file user input
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()            # goes to a file user input, maybe outdated, more like an example




def user_input_game(_numbers, _pointer_x, _pointer_y, _state):
    user_input = _Getch().__call__()
    if user_input == 'w':       # game has to be played with wasd cause the arrow keys are too difficult to get
        _pointer_y = (_pointer_y + (9-1)) % 9 # add 9 to avoid problems with mod9 decrement 1
    elif user_input == 's':
        _pointer_y = (_pointer_y + (9+1)) % 9 # add 9 to avoid problems with mod9 increment 1
    elif user_input == 'd':
        _pointer_x = (_pointer_x + (9+1)) % 9 # add 9 to avoid problems with mod9 increment 1
    elif user_input == 'a':
        _pointer_x = (_pointer_x + (9-1)) % 9 # add 9 to avoid problems with mod9 decrement 1
    elif user_input == 'q':
        _state = "lobby"
    elif user_input == '1':
        _numbers[_pointer_y][_pointer_x] = int(user_input)
    elif user_input == '2':
        _numbers[_pointer_y][_pointer_x] = int(user_input)
    elif user_input == '3':
        _numbers[_pointer_y][_pointer_x] = int(user_input)
    elif user_input == '4':
        _numbers[_pointer_y][_pointer_x] = int(user_input)
    elif user_input == '5':
        _numbers[_pointer_y][_pointer_x] = int(user_input)
    elif user_input == '6':
        _numbers[_pointer_y][_pointer_x] = int(user_input)
    elif user_input == '7':
        _numbers[_pointer_y][_pointer_x] = int(user_input)
    elif user_input == '8':
        _numbers[_pointer_y][_pointer_x] = int(user_input)
    elif user_input == '9':
        _numbers[_pointer_y][_pointer_x] = int(user_input)
    # maybe the statement below should be excluded to the main menue
    elif user_input == 't':
        logic.test_sudoku(_numbers)
    return _numbers, _pointer_x, _pointer_y, _state
