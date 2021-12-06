# This file contains the real algorithm for testing if all the numbers are correct and to solve the Sudoku recursively

import numpy as np

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
        #print("Das Objekt selbst: " + str(_numbers[idx]) + " und der Index: " + str(idx))
        if _numbers[idx] == 0:
            _numbers[idx] = 1
            while(_numbers[idx] < 10):
                test_result = test_sudoku(_numbers)
                if(test_result == -1):
                    #print("noch nicht fertig, eine ebene weiter runter")
                    test_result = solve_sudoku(_numbers)
                elif(test_result == 0):
                    #print("One step further as its correct")
                    return test_result

                if(test_result == 1):
                    #print("Zahl falsch gelöst: " + str(_numbers[idx]))
                    _numbers[idx] = (_numbers[idx]+1)
                    #print("neuer wert: " + str(_numbers[idx]))
            _numbers[idx] = 0
            return 1
    return test_sudoku(_numbers)
