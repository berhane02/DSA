import pytest
from merge_intervals import Solution

class TestMerge:
    def test_example1(self):
        sol = Solution()
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = sol.merge(intervals)
        assert result == [[1, 6], [8, 10], [15, 18]]

    def test_example2(self):
        sol = Solution()
        intervals = [[1, 4], [4, 5]]
        result = sol.merge(intervals)
        assert result == [[1, 5]]

    def test_no_overlap(self):
        sol = Solution()
        intervals = [[1, 2], [3, 4], [5, 6]]
        result = sol.merge(intervals)
        assert result == [[1, 2], [3, 4], [5, 6]]

    def test_all_overlap(self):
        sol = Solution()
        intervals = [[1, 4], [2, 3], [3, 5]]
        result = sol.merge(intervals)
        assert result == [[1, 5]]

    def test_single_interval(self):
        sol = Solution()
        intervals = [[1, 4]]
        result = sol.merge(intervals)
        assert result == [[1, 4]]

    def test_empty_list(self):
        sol = Solution()
        intervals = []
        result = sol.merge(intervals)
        assert result == []

    def test_contained_interval(self):
        sol = Solution()
        intervals = [[1, 10], [2, 3], [4, 5]]
        result = sol.merge(intervals)
        assert result == [[1, 10]]

    def test_touching_intervals(self):
        sol = Solution()
        intervals = [[1, 2], [2, 3], [3, 4]]
        result = sol.merge(intervals)
        assert result == [[1, 4]]

