class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_div_sum(n):
            divisors = set()
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                if len(divisors) > 4:
                    return 0  # early stop
                    
            return sum(divisors) if len(divisors) == 4 else 0
        return sum(get_div_sum(num) for num in nums)