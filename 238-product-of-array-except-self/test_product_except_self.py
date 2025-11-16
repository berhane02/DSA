import pytest
from product_of_array_except_self import Solution

class TestProductExceptSelf:
    def test_example1(self):
        sol = Solution()
        assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_example2(self):
        sol = Solution()
        assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    def test_two_elements(self):
        sol = Solution()
        assert sol.productExceptSelf([1, 2]) == [2, 1]

    def test_three_elements(self):
        sol = Solution()
        assert sol.productExceptSelf([2, 3, 4]) == [12, 8, 6]

    def test_with_zeros(self):
        sol = Solution()
        result = sol.productExceptSelf([0, 0])
        assert result == [0, 0]

    def test_negative_numbers(self):
        sol = Solution()
        assert sol.productExceptSelf([-1, -2, -3]) == [6, 3, 2]

    def test_single_zero(self):
        sol = Solution()
        result = sol.productExceptSelf([1, 0, 3, 4])
        assert result == [0, 12, 0, 0]

    def test_all_ones(self):
        sol = Solution()
        assert sol.productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]

