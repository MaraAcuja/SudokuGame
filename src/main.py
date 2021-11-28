## This is the main program holding the basic sequence and getting the input


## Think big für UML,
## vielleicht als App / Spielestore mit anderen Spielen

## DDD
## 5-10 domains with labeled connections
## filled out cards with characterstics

# import of libraries
import time             # just for debugging and nowerdays also for graphical output after testing
import numpy as np

# import of own functions
import init
import user_interactions as uin
import user_output as uout
import sudoku_logic as logic


def game_control(_playing_before):      # stays here or goes to a file control.py
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

if __name__ == '__main__':
    numbers = (9,9)
    numbers = np.zeros(numbers, dtype=int)
    init.initialise_sudoku_with_numbers(numbers)
    pointer_x = 4
    pointer_y = 6

    for i in range(9):
        print(numbers[i])

    while(True):
        game_state = 0
        uout.draw_menue(game_state)
        game_state = game_control(game_state)
            # save, load, initialise, solve, test on two times same number in row / column / square
        while(game_state == "play"):
            uout.draw_menue(game_state)
            uout.update_game_field(numbers, pointer_x, pointer_y)
            numbers, pointer_x, pointer_y, game_state = uin.user_input_game(numbers, pointer_x, pointer_y,game_state)
            # get user interaction
            # interpret user action
            #time.sleep(2)
            #break
        if game_state == "test":
            tested = logic.test_sudoku(numbers)
            if tested == 0:
                print("The SUDOKU is solved correct!")
            elif tested == 1:
                print("There is a mistake in the SUDOKU")
            elif tested == -1:
                print("The SUDOKU is not yet finished but correct so far.")
            time.sleep(3)
        if game_state == "solve":
            logic.solve_sudoku(numbers)
            print(numbers)
            uout.draw_menue(game_state)
            uout.update_game_field(numbers, pointer_x, pointer_y)

        if game_state == "exit":
            break
