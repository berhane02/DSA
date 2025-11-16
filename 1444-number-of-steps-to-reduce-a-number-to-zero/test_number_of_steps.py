import pytest
from number_of_steps_to_reduce_a_number_to_zero import Solution

class TestNumberOfSteps:
    def test_example1(self):
        sol = Solution()
        assert sol.numberOfSteps(14) == 6

    def test_example2(self):
        sol = Solution()
        assert sol.numberOfSteps(8) == 4

    def test_example3(self):
        sol = Solution()
        assert sol.numberOfSteps(123) == 12

    def test_zero(self):
        sol = Solution()
        assert sol.numberOfSteps(0) == 0

    def test_one(self):
        sol = Solution()
        assert sol.numberOfSteps(1) == 1

    def test_power_of_two(self):
        sol = Solution()
        assert sol.numberOfSteps(16) == 5  # 16 -> 8 -> 4 -> 2 -> 1 -> 0

    def test_odd_number(self):
        sol = Solution()
        assert sol.numberOfSteps(7) == 5  # 7 -> 6 -> 3 -> 2 -> 1 -> 0

    def test_large_number(self):
        sol = Solution()
        result = sol.numberOfSteps(1000)
        assert result > 0

