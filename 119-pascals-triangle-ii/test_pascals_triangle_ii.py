import pytest
from pascals_triangle_ii import Solution

class TestGetRow:
    def test_example1(self):
        sol = Solution()
        assert sol.getRow(3) == [1, 3, 3, 1]

    def test_example2(self):
        sol = Solution()
        assert sol.getRow(0) == [1]

    def test_example3(self):
        sol = Solution()
        assert sol.getRow(1) == [1, 1]

    def test_row_2(self):
        sol = Solution()
        assert sol.getRow(2) == [1, 2, 1]

    def test_row_4(self):
        sol = Solution()
        assert sol.getRow(4) == [1, 4, 6, 4, 1]

    def test_row_5(self):
        sol = Solution()
        assert sol.getRow(5) == [1, 5, 10, 10, 5, 1]

    def test_larger_row(self):
        sol = Solution()
        result = sol.getRow(10)
        assert len(result) == 11
        assert result[0] == 1
        assert result[-1] == 1
        assert result[5] == 252  # middle element for row 10

