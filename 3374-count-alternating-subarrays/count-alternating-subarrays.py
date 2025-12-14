class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        length = 1

        ans = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                length += 1
            else:
                length = 1
            ans += length

        return ans