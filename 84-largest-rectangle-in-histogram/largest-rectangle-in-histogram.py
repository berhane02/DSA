class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        stk = []

        for i, height in enumerate(heights):
            start = i
            while stk and height < stk[-1][0]:
                h , j = stk.pop()
                w = i-j
                area = max(area, h*w)
                start = j
            stk.append((height,start))

        while stk:
            h, j = stk.pop()
            w = n-j
            area = max(area, h*w)

        return area