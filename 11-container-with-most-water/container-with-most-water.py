class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        maxArea = 0

        while l<r:
            h = min(height[l], height[r])
            area = h*(r-l)
            maxArea = max(maxArea, area)

            if height[l] > height[r]:
                r -=1
            else:
                l +=1
        return maxArea