class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        indx = [inf]*(amount+1)
        
        indx[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i-c >=0:
                    indx[i] = min(indx[i],indx[i-c]+1)
        if indx[amount] != inf: return indx[amount]
        else: return -1