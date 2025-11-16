import pytest
from best_time_to_buy_and_sell_stock import Solution

class TestMaxProfit:
    def test_example1(self):
        sol = Solution()
        assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    def test_example2(self):
        sol = Solution()
        assert sol.maxProfit([7, 6, 4, 3, 1]) == 0

    def test_single_day(self):
        sol = Solution()
        assert sol.maxProfit([1]) == 0

    def test_two_days_profit(self):
        sol = Solution()
        assert sol.maxProfit([1, 2]) == 1

    def test_two_days_loss(self):
        sol = Solution()
        assert sol.maxProfit([2, 1]) == 0

    def test_max_profit_at_end(self):
        sol = Solution()
        assert sol.maxProfit([1, 2, 3, 4, 5]) == 4

    def test_max_profit_in_middle(self):
        sol = Solution()
        assert sol.maxProfit([3, 2, 6, 5, 0, 3]) == 4

    def test_all_same_price(self):
        sol = Solution()
        assert sol.maxProfit([5, 5, 5, 5]) == 0

