class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def four_divisor_sum(n):
            divisors = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                    if len(divisors) > 4:
                        return 0
            return sum(divisors) if len(divisors) == 4 else 0

        ans = 0
        for n in nums:
            ans += four_divisor_sum(n)
        return ans