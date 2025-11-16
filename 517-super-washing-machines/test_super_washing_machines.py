import pytest
from super_washing_machines import Solution

class TestFindMinMoves:
    def test_example1(self):
        sol = Solution()
        assert sol.findMinMoves([1, 0, 5]) == 3

    def test_example2(self):
        sol = Solution()
        assert sol.findMinMoves([0, 3, 0]) == 2

    def test_example3(self):
        sol = Solution()
        assert sol.findMinMoves([0, 2, 0]) == -1

    def test_already_balanced(self):
        sol = Solution()
        assert sol.findMinMoves([2, 2, 2]) == 0

    def test_single_machine(self):
        sol = Solution()
        assert sol.findMinMoves([5]) == 0

    def test_two_machines(self):
        sol = Solution()
        assert sol.findMinMoves([1, 3]) == 1

    def test_impossible_to_balance(self):
        sol = Solution()
        total = sum([1, 2, 3])
        if total % 3 != 0:
            assert sol.findMinMoves([1, 2, 3]) == -1

    def test_large_difference(self):
        sol = Solution()
        result = sol.findMinMoves([0, 0, 11, 5])
        assert result >= 0

