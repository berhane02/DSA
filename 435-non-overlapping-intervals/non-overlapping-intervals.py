class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # sort by end time

        

        end = float('-inf')

        count = 0

        

        for start, finish in intervals:

            if start >= end:

                end = finish  # keep interval

            else:

                count += 1  # remove interval

        

        return count