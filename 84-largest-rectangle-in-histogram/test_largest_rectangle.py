import pytest
from largest_rectangle_in_histogram import Solution

class TestLargestRectangleArea:
    def test_example1(self):
        sol = Solution()
        assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10

    def test_example2(self):
        sol = Solution()
        assert sol.largestRectangleArea([2, 4]) == 4

    def test_single_bar(self):
        sol = Solution()
        assert sol.largestRectangleArea([5]) == 5

    def test_increasing_heights(self):
        sol = Solution()
        assert sol.largestRectangleArea([1, 2, 3, 4, 5]) == 9

    def test_decreasing_heights(self):
        sol = Solution()
        assert sol.largestRectangleArea([5, 4, 3, 2, 1]) == 9

    def test_all_same_height(self):
        sol = Solution()
        assert sol.largestRectangleArea([3, 3, 3, 3]) == 12

    def test_two_bars(self):
        sol = Solution()
        assert sol.largestRectangleArea([2, 1]) == 2

    def test_complex_case(self):
        sol = Solution()
        assert sol.largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12

