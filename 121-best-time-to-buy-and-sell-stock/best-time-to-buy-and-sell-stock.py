class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0

        l = len(prices)

        for i in range(1, l):
            if buy > prices[i]:
                buy = prices[i]
            elif prices[i]-buy>profit:
                profit = prices[i]-buy
        return profit
        