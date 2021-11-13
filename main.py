## This is the main program holding the basic sequence and getting the input


## Think big für UML,
## vielleicht als App / Spielestore mit anderen Spielen

## DDD
## 5-10 domains with labeled connections
## filled out cards with characterstics


import os   # importing for clearing screen  (cls())
import time # just for debugging
import numpy as np
import cv2

def draw_menue(state):          # goes to a file output.py
    os.system('clear')
    print("###############")
    print("# SUDOKU GAME #")
    print("###############")
    if state == "play":
        # Here comes the control user commands while playing the game
        print("Please use the following keys playing the game")
    else:
        print("\nWelcome! Do you want to play with me? You can play a SUDOKU.")
        print("Type PLAY to start a new game.")
        print("For solving the game, type SOLVE.")
        print("To leave the game, please type EXIT.")

def general_structure_game_field(numbers): ### maybe for documentation purposes  but outdated
    print("\n")
    print("               |               ")
    print("               V               ")
    print("    -------------------------  ")
    print("    |       |       |       |  ")
    print("    |       |       |       |  ")
    print("    |       |       |       |  ")
    print("    -------------------------  ")
    print("    |       |       |       |  ")
    print("    |       |       |       |  ")
    print(" -> |       | _     |       |  ")
    print("    -------------------------  ")
    print("    |       |       |       |  ")
    print("    |       |       |       |  ")
    print("    |       |       |       |  ")
    print("    -------------------------  ")

def update_game_field(_numbers, _pointer_x, _pointer_y):      # goes to a file output.py
    pt_x = _pointer_x%9
    pt_y = _pointer_y%9
    print("      ", end='')
    for i in range(0,pt_x):
        print("  ", end='')
    if pt_x > 5:
        print("    ", end='')
    elif pt_x > 2:
        print("  ", end='')
    print(" V")
    for i in range(9):
        if i%3 == 0:
            print("     -------------------------  ")
        if pt_y == i:
            print(" -> ", end='')
        else:
            print("    ", end='')
        for j in range(9):
            if j%3==0:
                print(" | " + str(_numbers[i][j] if _numbers[i][j] != 0 else " "), end='')
            else:
                print(" " + str(_numbers[i][j] if _numbers[i][j] != 0 else " "), end='')
        print(" |  ")
    print("     -------------------------  ")
def game_control(_playing_before):      # stays here or goes to a file control.py
    state = _playing_before
    key_input = input()
    print(key_input)
    if key_input == "PLAY" or key_input == "Play" or key_input == "play":
        state = "play"
    elif key_input == "SOLVE" or key_input == "solve" or key_input == "Solve":
        state = "solve"
    elif key_input == "TEST" or key_input == "test" or key_input == "Test":
        state = "test"
    elif key_input == "Exit" or key_input == "EXIT" or key_input == "exit":
        state = "exit"
    else:
        state = "lobby"
    return state

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
    #print("_pointer_x: " + str(_pointer_x))
    #print("_pointer_y: " + str(_pointer_y))
    user_input = _Getch().__call__()
#    user_input = cv2.waitKey(2)
    print(str(user_input))
    if user_input == 'w':       # game has to be played with wasd cause the arrow keys are too difficult to get
        #print("up")             # especially platform independent
        _pointer_y = (_pointer_y + (9-1)) % 9 # add 9 to avoid problems with mod9 decrement 1
    elif user_input == 's':
        #print("down")
        _pointer_y = (_pointer_y + (9+1)) % 9 # add 9 to avoid problems with mod9 increment 1
    elif user_input == 'd':
        #print("right")
        _pointer_x = (_pointer_x + (9+1)) % 9 # add 9 to avoid problems with mod9 increment 1
    elif user_input == 'a':
        #print("left")
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
        test_sudoku(_numbers)
    return _numbers, _pointer_x, _pointer_y, _state

def test_sudoku(_numbers):
    error = 0
    # test if same element in row and column
    for i in range(9):
        for k in range(9):
            for l in range(9):
                if (((_numbers[i][k] == _numbers[i][l] and k!=l) or (_numbers[i][k] == _numbers[l][k] and i!=l)) and _numbers[i][k] !=0):
                    error = 1
                              # prevent from check against same element
                                # \
                              # prevent from empty element
#                                and _numbers[i][k] != 0):

                    # test if same element in squares
    for n in range(3):  # select the square
        for o in range(3): # select the square
            for i in range(3): # select the element to test
                for k in range(3): # select the element to test
                    for l in range(3): # select the element to test against
                        for m in range(3): # select the element to test against
                            if _numbers[i+n*3][k+o*3] == _numbers[l+n*3][m+o*3]\
                                        and not (i==l and k==m) \
                                        and _numbers[i+n*3][k+o*3] != 0:
                                error = 1
    # test if Sudoku is solved completely
    if error < 1:
        for i in range(9):
            for k in range(9):
                if _numbers[i][k] == 0: error = -1
    return error

def solve_sudoku(_numbers):
    for idx, i in np.ndenumerate(_numbers):
        print("Das Objekt selbst: " + str(_numbers[idx]) + " und der Index: " + str(idx))
        if _numbers[idx] == 0:
            _numbers[idx] = 1
            while(_numbers[idx] < 10):
                test_result = test_sudoku(_numbers)
                if(test_result == -1):
                    print("noch nicht fertig, eine ebene weiter runter")
                    test_result = solve_sudoku(_numbers)
                elif(test_result == 0):
                    print("One step further as its correct")
                    return test_result

                if(test_result == 1):
                    print("Zahl falsch gelöst: " + str(_numbers[idx]))
                    _numbers[idx] = (_numbers[idx]+1)
                    print("neuer wert: " + str(_numbers[idx]))
            _numbers[idx] = 0
            return 1
    return test_sudoku(_numbers)

def initialise_sudoku_with_numbers(_numbers):
    _numbers[0][0] = 0
    _numbers[0][1] = 2
    _numbers[0][2] = 6
    _numbers[0][3] = 0
    _numbers[0][4] = 0
    _numbers[0][5] = 0
    _numbers[0][6] = 8
    _numbers[0][7] = 1
    _numbers[0][8] = 0

    _numbers[1][0] = 3
    _numbers[1][1] = 0
    _numbers[1][2] = 0
    _numbers[1][3] = 7
    _numbers[1][4] = 0
    _numbers[1][5] = 8
    _numbers[1][6] = 0
    _numbers[1][7] = 0
    _numbers[1][8] = 6

    _numbers[2][0] = 4
    _numbers[2][1] = 0
    _numbers[2][2] = 0
    _numbers[2][3] = 0
    _numbers[2][4] = 5
    _numbers[2][5] = 0
    _numbers[2][6] = 0
    _numbers[2][7] = 0
    _numbers[2][8] = 7

    _numbers[3][0] = 0
    _numbers[3][1] = 5
    _numbers[3][2] = 0
    _numbers[3][3] = 1
    _numbers[3][4] = 0
    _numbers[3][5] = 7
    _numbers[3][6] = 0
    _numbers[3][7] = 9
    _numbers[3][8] = 0

    _numbers[4][0] = 0
    _numbers[4][1] = 0
    _numbers[4][2] = 3
    _numbers[4][3] = 9
    _numbers[4][4] = 0
    _numbers[4][5] = 5
    _numbers[4][6] = 1
    _numbers[4][7] = 0
    _numbers[4][8] = 0

    _numbers[5][0] = 0
    _numbers[5][1] = 4
    _numbers[5][2] = 0
    _numbers[5][3] = 3
    _numbers[5][4] = 0
    _numbers[5][5] = 2
    _numbers[5][6] = 0
    _numbers[5][7] = 5
    _numbers[5][8] = 0

    _numbers[6][0] = 1
    _numbers[6][1] = 0
    _numbers[6][2] = 0
    _numbers[6][3] = 0
    _numbers[6][4] = 3
    _numbers[6][5] = 0
    _numbers[6][6] = 0
    _numbers[6][7] = 0
    _numbers[6][8] = 2

    _numbers[7][0] = 5
    _numbers[7][1] = 0
    _numbers[7][2] = 0
    _numbers[7][3] = 2
    _numbers[7][4] = 0
    _numbers[7][5] = 4
    _numbers[7][6] = 0
    _numbers[7][7] = 0
    _numbers[7][8] = 9

    _numbers[8][0] = 0
    _numbers[8][1] = 3
    _numbers[8][2] = 8
    _numbers[8][3] = 0
    _numbers[8][4] = 0
    _numbers[8][5] = 0
    _numbers[8][6] = 4
    _numbers[8][7] = 6
    _numbers[8][8] = 0

    return _numbers

if __name__ == '__main__':
    numbers = (9,9)
    numbers = np.zeros(numbers, dtype=int)
    #for i in range(9):
    #    numbers.append([])
    #    for j in range(9):
    #        numbers[i].append(((i+j)%9)+1)
    initialise_sudoku_with_numbers(numbers)
    #numbers[4][5] = " "
    pointer_x = 4
    pointer_y = 6

    for i in range(9):
        print(numbers[i])

    while(True):
        game_state = 0
        draw_menue(game_state)
        game_state = game_control(game_state)
            # save, load, initialise, solve, test on two times same number in row / column / square
        while(game_state == "play"):
            draw_menue(game_state)
            update_game_field(numbers, pointer_x, pointer_y)
            #while(True):
            numbers, pointer_x, pointer_y, game_state = user_input_game(numbers, pointer_x, pointer_y,game_state)
            # get user interaction
            # interpret user action
            #time.sleep(2)
            #break
        if game_state == "test":
            tested = test_sudoku(numbers)
            if tested == 0:
                print("The SUDOKU is solved correct!")
            elif tested == 1:
                print("There is a mistake in the SUDOKU")
            elif tested == -1:
                print("The SUDOKU is not yet finished but correct so far.")
            time.sleep(3)
        if game_state == "solve":
            solve_sudoku(numbers)
            print(numbers)
            draw_menue(game_state)
            update_game_field(numbers, pointer_x, pointer_y)

        if game_state == "exit":
            break





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
