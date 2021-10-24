from typing import List
import unittest

class Solution:
    def is_in_boundary(self, grid: List[List[int]], row, col) -> int:
        row_boundary = len(grid)
        col_boundary = len(grid[0])
        
        return 0 <= row < row_boundary and 0 <= col < col_boundary
    
    def explore_island_chain(self, grid: List[List[int]], row: int, col: int, num_cells: List[int]) -> int:
        if self.is_in_boundary(grid, row, col) and grid[row][col] == 1:
            grid[row][col] = 0
            num_cells[0] += 1
            self.explore_island_chain(grid, row - 1, col, num_cells)
            self.explore_island_chain(grid, row, col + 1, num_cells)
            self.explore_island_chain(grid, row, col - 1, num_cells)
            self.explore_island_chain(grid, row + 1, col, num_cells)

        return num_cells[0]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_cells = self.explore_island_chain(grid, i, j, [0])
                    if num_cells > max:
                        max = num_cells
        
        return max

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

        self.grid1 = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        self.grid1_expected = 6

        self.grid2 = [
            [0,0,1],
            [0,1,0],
            [1,0,0]
        ]
        self.grid2_expected = 1

        self.grid3 = [[1]]
        self.grid3_expected = 1

        self.grid4 = [[0,0,0]]
        self.grid4_expected = 0

        return super().setUp()
    
    def test_solution(self) -> None:
        actual_1 = self.sol.maxAreaOfIsland(self.grid1)
        actual_2 = self.sol.maxAreaOfIsland(self.grid2)
        actual_3 = self.sol.maxAreaOfIsland(self.grid3)
        actual_4 = self.sol.maxAreaOfIsland(self.grid4)

        self.assertEqual(self.grid1_expected, actual_1)
        self.assertEqual(self.grid2_expected, actual_2)
        self.assertEqual(self.grid3_expected, actual_3)
        self.assertEqual(self.grid4_expected, actual_4)

unittest.main()