class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def ways(expr):
            results = []
            for i, c in enumerate(expr):
                if c in "+-*":
                    left = ways(expr[:i])
                    right = ways(expr[i+1:])
                    for l in left:
                        for r in right:
                            if c == '+':
                                results.append(l + r)
                            elif c == '-':
                                results.append(l - r)
                            else:  # '*'
                                results.append(l * r)
            if not results:  # base case: no operator, just a number
                results.append(int(expr))
            return results

        return ways(expression)