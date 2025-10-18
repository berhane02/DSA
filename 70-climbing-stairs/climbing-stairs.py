class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        res = [1,2]

        for i in range (2, n):
            res.append(res[i-1]+res[i-2])
        return res[-1]