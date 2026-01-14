class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        index = [float(inf)]* (amount+1)
        index[0]=0

        for c in coins:
            for i in range(c,amount+1):
                if i-c>=0:
                    index[i] = min(index[i],index[i-c]+1)
        
        return index[amount] if index[amount] != float(inf) else -1