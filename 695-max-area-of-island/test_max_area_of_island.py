import pytest
from max_area_of_island import Solution

class TestMaxAreaOfIsland:
    def test_example1(self):
        sol = Solution()
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]
        assert sol.maxAreaOfIsland(grid) == 6

    def test_example2(self):
        sol = Solution()
        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        assert sol.maxAreaOfIsland(grid) == 0

    def test_single_island(self):
        sol = Solution()
        grid = [[1]]
        assert sol.maxAreaOfIsland(grid) == 1

    def test_no_islands(self):
        sol = Solution()
        grid = [[0, 0], [0, 0]]
        assert sol.maxAreaOfIsland(grid) == 0

    def test_multiple_islands(self):
        sol = Solution()
        grid = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        assert sol.maxAreaOfIsland(grid) == 1

    def test_connected_island(self):
        sol = Solution()
        grid = [
            [1, 1],
            [1, 1]
        ]
        assert sol.maxAreaOfIsland(grid) == 4

