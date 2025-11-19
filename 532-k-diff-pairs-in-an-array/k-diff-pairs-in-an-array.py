class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        unix = Counter(nums)
        pair = set()
        if k == 0:
            return len(list(filter(lambda x: unix[x]>1, unix)))
        else:

            for i in range(len(nums)):
                if nums[i]+k in unix:
                    pair.add(tuple(sorted((nums[i],nums[i]+k))))
                elif nums[i]-k in unix:
                    pair.add(tuple(sorted((nums[i],nums[i]-k))))
            return len(pair)