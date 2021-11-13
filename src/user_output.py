## This is the file for the graphical output in the shell

import os

# Functional Programming:
# All functions within this file are final, hence the input variables aren't overwritten. The
# functions work completely side-effect-free. They are also a special case as they do not have
# a return value.

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

# Functional Programming
# The function below is a good example as it works just with variables within the function and
# neither the input variables nor any other variables or data is changed. So, it doesn't matter
# how often or at what point of the algorithms this function is called it won't ever interfere
# with another function. This makes it a side-effect-free function.

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
