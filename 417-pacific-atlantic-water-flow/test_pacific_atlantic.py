import pytest
from pacific_atlantic_water_flow import Solution

def normalize_result(result):
    """Helper to normalize result for comparison"""
    return sorted([tuple(cell) for cell in result])

class TestPacificAtlantic:
    def test_example1(self):
        sol = Solution()
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        result = sol.pacificAtlantic(heights)
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        assert normalize_result(result) == normalize_result(expected)

    def test_example2(self):
        sol = Solution()
        heights = [[1]]
        result = sol.pacificAtlantic(heights)
        assert normalize_result(result) == normalize_result([[0, 0]])

    def test_single_row(self):
        sol = Solution()
        heights = [[1, 2, 3, 4, 5]]
        result = sol.pacificAtlantic(heights)
        assert normalize_result(result) == normalize_result([[0, 0], [0, 4]])

    def test_single_column(self):
        sol = Solution()
        heights = [[1], [2], [3], [4], [5]]
        result = sol.pacificAtlantic(heights)
        assert normalize_result(result) == normalize_result([[0, 0], [4, 0]])

    def test_all_same_height(self):
        sol = Solution()
        heights = [[1, 1], [1, 1]]
        result = sol.pacificAtlantic(heights)
        assert normalize_result(result) == normalize_result([[0, 0], [0, 1], [1, 0], [1, 1]])

