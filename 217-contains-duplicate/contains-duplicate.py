class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # s = set()
        # for n in nums:
        #     if n in s:
        #         return True
        #     s.add(n)
        # return False
        #return len(nums) != len(set(nums))
        dist = {}
        for i in range(len(nums)):
            if nums[i] in dist:
                return True
            dist[nums[i]] = i
        return False

print(Solution().containsDuplicate([1,2,3,1]))