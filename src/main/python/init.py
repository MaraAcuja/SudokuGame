# This file is to initialise the play grid with numbers. It will be outdated when a save and load function is implemented

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
