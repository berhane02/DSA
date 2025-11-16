import pytest
from set_mismatch import Solution

class TestFindErrorNums:
    def test_example1(self):
        sol = Solution()
        result = sol.findErrorNums([1, 2, 2, 4])
        assert set(result) == {2, 3}

    def test_example2(self):
        sol = Solution()
        result = sol.findErrorNums([1, 1])
        assert set(result) == {1, 2}

    def test_duplicate_at_start(self):
        sol = Solution()
        result = sol.findErrorNums([2, 2])
        assert set(result) == {2, 1}

    def test_duplicate_at_end(self):
        sol = Solution()
        result = sol.findErrorNums([1, 2, 3, 3])
        assert set(result) == {3, 4}

    def test_small_array(self):
        sol = Solution()
        result = sol.findErrorNums([2, 2])
        assert set(result) == {2, 1}

    def test_larger_array(self):
        sol = Solution()
        result = sol.findErrorNums([1, 2, 3, 4, 5, 5])
        assert set(result) == {5, 6}

    def test_duplicate_in_middle(self):
        sol = Solution()
        result = sol.findErrorNums([1, 3, 3, 4])
        assert set(result) == {3, 2}

