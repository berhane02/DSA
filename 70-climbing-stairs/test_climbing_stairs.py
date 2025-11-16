import pytest
from climbing_stairs import Solution

class TestClimbStairs:
    def test_example1(self):
        sol = Solution()
        assert sol.climbStairs(2) == 2

    def test_example2(self):
        sol = Solution()
        assert sol.climbStairs(3) == 3

    def test_n_equals_1(self):
        sol = Solution()
        assert sol.climbStairs(1) == 1

    def test_n_equals_4(self):
        sol = Solution()
        assert sol.climbStairs(4) == 5

    def test_n_equals_5(self):
        sol = Solution()
        assert sol.climbStairs(5) == 8

    def test_n_equals_6(self):
        sol = Solution()
        assert sol.climbStairs(6) == 13

    def test_larger_n(self):
        sol = Solution()
        assert sol.climbStairs(10) == 89

    def test_fibonacci_sequence(self):
        sol = Solution()
        # Verify it follows Fibonacci sequence
        assert sol.climbStairs(1) == 1
        assert sol.climbStairs(2) == 2
        assert sol.climbStairs(3) == 3
        assert sol.climbStairs(4) == 5
        assert sol.climbStairs(5) == 8

