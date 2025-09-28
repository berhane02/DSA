class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        s = set()
        duplicate = 0
        for n in nums:
            if n in s:
                duplicate = n
            s.add(n)
        for i in range(len(nums)):
            if i+1 not in s:
                return [duplicate, i+1]