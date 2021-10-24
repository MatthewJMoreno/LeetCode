from typing import List
import unittest

class Solution:
    def is_in_boundary(self, image: List[List[int]], row: int, col: int) -> bool:
        row_boundary: int = len(image)
        col_boundary: int = len(image[0])

        return 0 <= row < row_boundary and 0 <= col < col_boundary

    def flood_fill_recursive(self, image: List[List[int]], row: int, col: int, new_color: int, curr_color: int) -> None:
        if self.is_in_boundary(image, row, col) and image[row][col] == curr_color:
            image[row][col] = new_color
            print(image)
            self.flood_fill_recursive(image, row - 1, col, new_color, curr_color)
            self.flood_fill_recursive(image, row, col + 1, new_color, curr_color)
            self.flood_fill_recursive(image, row + 1, col, new_color, curr_color)
            self.flood_fill_recursive(image, row, col - 1, new_color, curr_color)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        curr_color = image[sr][sc]

        if curr_color == newColor:
            return image

        self.flood_fill_recursive(image, sr, sc, newColor, curr_color)
        print(image)
        return image

class TestSolutionMethods(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.image1 = [
            [0, 0, 1, 2],
            [2, 2, 2, 2],
            [2, 0, 0, 3],
            [4, 2, 2, 1]
        ]

        self.image2 = [
            [1,1,1],
            [1,1,0],
            [1,0,1]
        ]

        #expected when sr = sc = 1
        self.image1_expected = [
            [0, 0, 1, 5],
            [5, 5, 5, 5],
            [5, 0, 0, 3],
            [4, 2, 2, 1]
        ]

        #exptected when sr = sc = 1
        self.image2_expected = [
            [2, 2, 2],
            [2, 2, 0],
            [2, 0, 1]
        ]
    
    def compare_matricies(self, A: List[List[int]], B: List[List[int]]) -> bool:
        for i in range(len(A)):
            if A[i] != B[i]:
                return False

        return True

    def test_boundary(self):
        row_1 = 4
        col_1 = 10
        expected1 = False
        actual1 = self.sol.is_in_boundary(self.image1, row_1, col_1)
        self.assertEqual(expected1, actual1)

        row_2 = 3
        col_2 = 4
        expected2 = False
        actual2 = self.sol.is_in_boundary(self.image1, row_2, col_2)
        self.assertEqual(expected2, actual2)

        row_3 = 3
        col_3 = 3
        expected3 = True
        actual3 = self.sol.is_in_boundary(self.image1, row_3, col_3)
        self.assertEqual(expected3, actual3)

    def test_matrix_compare(self):
        A = [[2, 3], [4, 5]]
        B = [[2, 3], [4, 5]]
        C = [[2, 3], [5, 5]]
        D = [[2, 3], [4, 5]]
        
        expected1 = True
        acutal1 = self.compare_matricies(A, B)
        self.assertEqual(expected1, acutal1)

        expected1 = False
        acutal1 = self.compare_matricies(C, D)
        self.assertEqual(expected1, acutal1)

    def test_solution(self):
        #self.sol.floodFill(self.image1, 1, 1, 5)
        #self.assertEqual(self.image1_expected, self.image1)

        self.sol.floodFill(self.image2, 1, 1, 2)
        self.assertEqual(self.image2_expected, self.image2)
unittest.main()