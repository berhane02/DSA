class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = defaultdict(int)
            left = 0
            result = 0
            for right, num in enumerate(nums):
                if count[num] == 0:
                    k -= 1
                count[num] += 1
                
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                    
                result += right - left + 1
            return result
    
        return atMost(k) - atMost(k - 1)