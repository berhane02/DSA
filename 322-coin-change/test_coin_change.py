import pytest
from coin_change import Solution

class TestCoinChange:
    def test_example1(self):
        sol = Solution()
        assert sol.coinChange([1, 2, 5], 11) == 3

    def test_example2(self):
        sol = Solution()
        assert sol.coinChange([2], 3) == -1

    def test_example3(self):
        sol = Solution()
        assert sol.coinChange([1], 0) == 0

    def test_exact_match(self):
        sol = Solution()
        assert sol.coinChange([1, 2, 5], 5) == 1

    def test_impossible(self):
        sol = Solution()
        assert sol.coinChange([2, 5], 3) == -1

    def test_single_coin(self):
        sol = Solution()
        assert sol.coinChange([1], 5) == 5

    def test_large_amount(self):
        sol = Solution()
        assert sol.coinChange([1, 2, 5], 100) == 20

    def test_greedy_fails(self):
        sol = Solution()
        # Greedy would give 3 (25+25+25) but optimal is 2 (25+5)
        assert sol.coinChange([1, 5, 25], 30) == 2

