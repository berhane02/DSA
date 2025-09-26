class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            dif = target-nums[i]
            if dif in dict:
                return [dict[dif],i]
            dict[nums[i]] = i