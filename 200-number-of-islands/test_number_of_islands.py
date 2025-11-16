import pytest
from number_of_islands import Solution

class TestNumIslands:
    def test_example1(self):
        sol = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        assert sol.numIslands(grid) == 1

    def test_example2(self):
        sol = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        assert sol.numIslands(grid) == 3

    def test_no_islands(self):
        sol = Solution()
        grid = [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]
        ]
        assert sol.numIslands(grid) == 0

    def test_all_islands(self):
        sol = Solution()
        grid = [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"]
        ]
        assert sol.numIslands(grid) == 1

    def test_single_cell_island(self):
        sol = Solution()
        grid = [["1"]]
        assert sol.numIslands(grid) == 1

    def test_single_cell_water(self):
        sol = Solution()
        grid = [["0"]]
        assert sol.numIslands(grid) == 0

    def test_diagonal_islands(self):
        sol = Solution()
        grid = [
            ["1", "0", "0"],
            ["0", "1", "0"],
            ["0", "0", "1"]
        ]
        assert sol.numIslands(grid) == 3

