import pytest
from container_with_most_water import Solution

class TestMaxArea:
    def test_example1(self):
        sol = Solution()
        assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_example2(self):
        sol = Solution()
        assert sol.maxArea([1, 1]) == 1

    def test_two_elements(self):
        sol = Solution()
        assert sol.maxArea([2, 3]) == 2

    def test_increasing_heights(self):
        sol = Solution()
        assert sol.maxArea([1, 2, 3, 4, 5]) == 6

    def test_decreasing_heights(self):
        sol = Solution()
        assert sol.maxArea([5, 4, 3, 2, 1]) == 6

    def test_same_heights(self):
        sol = Solution()
        assert sol.maxArea([3, 3, 3, 3, 3]) == 12

    def test_one_tall_bar(self):
        sol = Solution()
        assert sol.maxArea([1, 2, 1]) == 2

    def test_large_array(self):
        sol = Solution()
        heights = [i for i in range(100)]
        result = sol.maxArea(heights)
        assert result > 0

