import pytest
from transpose_matrix import Solution

class TestTranspose:
    def test_example1(self):
        sol = Solution()
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = sol.transpose(matrix)
        assert result == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    def test_example2(self):
        sol = Solution()
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = sol.transpose(matrix)
        assert result == [[1, 4], [2, 5], [3, 6]]

    def test_single_row(self):
        sol = Solution()
        matrix = [[1, 2, 3]]
        result = sol.transpose(matrix)
        assert result == [[1], [2], [3]]

    def test_single_column(self):
        sol = Solution()
        matrix = [[1], [2], [3]]
        result = sol.transpose(matrix)
        assert result == [[1, 2, 3]]

    def test_single_element(self):
        sol = Solution()
        matrix = [[5]]
        result = sol.transpose(matrix)
        assert result == [[5]]

    def test_rectangular_matrix(self):
        sol = Solution()
        matrix = [[1, 2], [3, 4], [5, 6]]
        result = sol.transpose(matrix)
        assert result == [[1, 3, 5], [2, 4, 6]]

