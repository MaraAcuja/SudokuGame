# This file contains the real algorithm for testing if all the numbers are correct and to solve the Sudoku recursively

import numpy as np

def test_sudoku(_numbers):
    error = 0

    # This is the first closured function. It just exists inside the test_sudoku()-function.
    def is_same_element_in_row_and_column(_error):
        # test if same element in row and column
        error = _error
        for i in range(9):
            for k in range(9):
                for l in range(9):
                    if (((_numbers[i][k] == _numbers[i][l] and k!=l) or (_numbers[i][k] == _numbers[l][k] and i!=l)) and _numbers[i][k] !=0):
                        error = 1
        return error

    # This is the second closured function.
    def is_same_element_in_squares(_error):
        # test if same element in squares
        error = _error
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
        return error

    # And here is a third one.
    def is_solved_completely(_error):
        # test if Sudoku is solved completely
        error = _error
        if error < 1:
            for i in range(9):
                for k in range(9):
                    if _numbers[i][k] == 0: error = -1
        return error

    error = is_same_element_in_row_and_column(error)
    error = is_same_element_in_squares(error)
    error = is_solved_completely(error)
    return error


def solve_sudoku(_numbers):
    for idx, i in np.ndenumerate(_numbers):
        if _numbers[idx] == 0:
            _numbers[idx] = 1
            while(_numbers[idx] < 10):
                test_result = test_sudoku(_numbers)
                if(test_result == -1):  # if the Sudoku is not yet completely solved continue with the next number
                    test_result = solve_sudoku(_numbers)    # the solving is recursively
                elif(test_result == 0): # if the Sudoku is solved completely, this routine returns to the first call
                    return test_result

                if(test_result == 1): # if the tried number doesn't fit to the rest of the Sudoku, try the next number
                    _numbers[idx] = (_numbers[idx]+1)
            _numbers[idx] = 0
            return 1 # Sudoku cannot be solved, there is a mistake inside
    return test_sudoku(_numbers)
