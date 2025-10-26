class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def memoize(func):
            cache = {}
            def wrapper(*args):
                if args in cache:
                    return cache[args]
                result = func(*args)
                cache[args] = result
                return result
            return wrapper
        
        
        n = len(s)
        
        @memoize
        def dp(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == right:
                return 1
            
            if s[left] == s[right]:
                return dp(left + 1, right - 1) + 2
            else:
                return max(dp(left, right - 1), dp(left + 1, right))
        
        return dp(0, n - 1)