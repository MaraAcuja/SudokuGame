import unittest
from src.main.python.sudoku_logic import test_sudoku
from src.main.python.sudoku_logic import solve_sudoku
import numpy as np





class SudokuLogicTest(unittest.TestCase):

    def test_correct_solved(self):
        numbers_correct = [[8, 4, 5, 9, 2, 6, 7, 1, 3],
                           [3, 1, 9, 8, 4, 7, 6, 5, 2],
                           [7, 6, 2, 3, 5, 1, 8, 9, 4],
                           [6, 5, 7, 4, 3, 2, 1, 8, 9],
                           [9, 3, 1, 7, 8, 5, 4, 2, 6],
                           [2, 8, 4, 1, 6, 9, 3, 7, 5],
                           [1, 7, 3, 5, 9, 4, 2, 6, 8],
                           [5, 2, 8, 6, 1, 3, 9, 4, 7],
                           [4, 9, 6, 2, 7, 8, 5, 3, 1]
                           ]
        x = [i for i in range(1,10)]
        numbers_wrong_column = [x,x,x,x,x,x,x,x,x]
        numbers_wrong_row = np.transpose(numbers_wrong_column)
        self.assertTrue(test_sudoku(numbers_correct) == 0)
        self.assertFalse(test_sudoku(numbers_wrong_column) == 0)
        self.assertFalse(test_sudoku(numbers_wrong_row) == 0)


    def test_solver(self):
        numbers_complete = np.array([[8, 4, 5, 9, 2, 6, 7, 1, 3],
                           [3, 1, 9, 8, 4, 7, 6, 5, 2],
                           [7, 6, 2, 3, 5, 1, 8, 9, 4],
                           [6, 5, 7, 4, 3, 2, 1, 8, 9],
                           [9, 3, 1, 7, 8, 5, 4, 2, 6],
                           [2, 8, 4, 1, 6, 9, 3, 7, 5],
                           [1, 7, 3, 5, 9, 4, 2, 6, 8],
                           [5, 2, 8, 6, 1, 3, 9, 4, 7],
                           [4, 9, 6, 2, 7, 8, 5, 3, 1]
                           ])
        x = [i for i in range(1, 10)]
        y = [0,0,0,0,0,0,0,0,0]
        numbers_one_row = np.array([x, y, y, y, y, y, y, y, y])
        numbers_wrong_column = np.array([x,x,x,x,x,x,x,x,x])
        self.assertTrue(solve_sudoku(numbers_complete) == 0)
        self.assertTrue(solve_sudoku(numbers_one_row) == 0)
        self.assertTrue(solve_sudoku(numbers_wrong_column) == 1)

