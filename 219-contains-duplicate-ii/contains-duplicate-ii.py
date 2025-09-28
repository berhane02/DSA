class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dist = {}
        for i in range(len(nums)):
            if nums[i] in dist:
                if abs(dist[nums[i]]- i) <=k:
                    return True

            dist[nums[i]]= i
        return False