class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        count = 1
        curr = 1
        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:
                curr += 1
            else:
                curr = 1
            count += curr
        return count