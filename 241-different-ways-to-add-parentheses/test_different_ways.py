import pytest
from different_ways_to_add_parentheses import Solution

class TestDiffWaysToCompute:
    def test_example1(self):
        sol = Solution()
        result = sol.diffWaysToCompute("2-1-1")
        assert set(result) == {0, 2}

    def test_example2(self):
        sol = Solution()
        result = sol.diffWaysToCompute("2*3-4*5")
        assert set(result) == {-34, -14, -10, -10, 10}

    def test_single_number(self):
        sol = Solution()
        assert sol.diffWaysToCompute("5") == [5]

    def test_simple_addition(self):
        sol = Solution()
        result = sol.diffWaysToCompute("1+1")
        assert result == [2]

    def test_simple_multiplication(self):
        sol = Solution()
        result = sol.diffWaysToCompute("2*3")
        assert result == [6]

    def test_simple_subtraction(self):
        sol = Solution()
        result = sol.diffWaysToCompute("5-2")
        assert result == [3]

    def test_three_operations(self):
        sol = Solution()
        result = sol.diffWaysToCompute("1+2*3")
        assert set(result) == {7, 9}

    def test_multiple_ways(self):
        sol = Solution()
        result = sol.diffWaysToCompute("1+1+1")
        assert set(result) == {3}

