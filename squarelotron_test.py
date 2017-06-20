import unittest
from squarelotron import *

class TestSquarelotron(unittest.TestCase):

    def test_make_squarelotron(self):
        self.assertEqual([[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]],
                         make_squarelotron(list(range(1, 26))))

    def test_make_list(self):
        self.assertEqual(list(range(1,26)), make_list(
                        [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]))

    def test_upside_down_flip(self):
        squarelotron = make_squarelotron(list(range(1, 26)))
        self.assertEqual([[21, 22, 23, 24, 25],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [1, 2, 3, 4, 5]], upside_down_flip(squarelotron, 'o'))
        self.assertEqual([[1, 2, 3, 4, 5],
                        [6, 17, 18, 19, 10],
                        [11, 12, 13, 14, 15],
                        [16, 7, 8, 9, 20],
                        [21, 22, 23, 24, 25]],
                         upside_down_flip(squarelotron, 'i'))

    def test_left_right_flip(self):
        squarelotron = make_squarelotron(list(range(1, 26)))
        self.assertEqual([[5, 2, 3, 4, 1],
                        [10, 7, 8, 9, 6],
                        [15, 12, 13, 14, 11],
                        [20, 17, 18, 19, 16],
                        [25, 22, 23, 24, 21]],
                         left_right_flip(squarelotron, 'o'))
        self.assertEqual([[1, 2, 3, 4, 5],
                        [6, 9, 8, 7, 10],
                        [11, 14, 13, 12, 15],
                        [16, 19, 18, 17, 20],
                        [21, 22, 23, 24, 25]],
                         left_right_flip(squarelotron, 'i'))

    def test_main_diagonal_flip(self):
        squarelotron = make_squarelotron(list(range(1,26)))
        
        self.assertEqual([[1, 6, 11, 16, 21],
                          [2, 7,  8, 9, 22],
                          [3, 12, 13, 14, 23],
                          [4, 17, 18, 19, 24],
                          [5, 10, 15, 20, 25]],
                         main_diagonal_flip(squarelotron, 'o'))

        self.assertEqual([[1, 2, 3, 4, 5],
                          [6, 7, 12, 17, 10],
                        [11, 8, 13, 18, 15],
                        [16, 9, 14, 19, 20],
                        [21, 22, 23, 24, 25]],
                         main_diagonal_flip(squarelotron, 'i'))

    def test_inverse_diagonal_flip(self):
        squarelotron = make_squarelotron(list(range(1,26)))

        self.assertEqual([[25, 20, 15, 10, 5],
                         [24, 7, 8, 9, 4],
                        [23, 12, 13, 14, 3],
                        [22, 17, 18, 19, 2],
                        [21, 16, 11, 6, 1]],
                         inverse_diagonal_flip(squarelotron, 'o'))
        

        self.assertEqual([[1, 2, 3, 4, 5],
                         [6, 19, 14, 9, 10],
                        [11, 18, 13, 8, 15],
                        [16, 17, 12, 7, 20],
                        [21, 22, 23, 24, 25]],
                         inverse_diagonal_flip(squarelotron, 'i'))
unittest.main()
