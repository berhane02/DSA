import pytest
from k_closest_points_to_origin import Solution

def normalize_result(result):
    """Helper to normalize result for comparison"""
    return sorted([tuple(point) for point in result])

class TestKClosest:
    def test_example1(self):
        sol = Solution()
        points = [[1, 3], [-2, 2]]
        k = 1
        result = sol.kClosest(points, k)
        assert normalize_result(result) == normalize_result([[-2, 2]])

    def test_example2(self):
        sol = Solution()
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        result = sol.kClosest(points, k)
        assert len(result) == 2
        assert normalize_result(result) == normalize_result([[3, 3], [-2, 4]])

    def test_single_point(self):
        sol = Solution()
        points = [[1, 1]]
        k = 1
        result = sol.kClosest(points, k)
        assert result == [[1, 1]]

    def test_k_equals_length(self):
        sol = Solution()
        points = [[1, 1], [2, 2], [3, 3]]
        k = 3
        result = sol.kClosest(points, k)
        assert len(result) == 3

    def test_origin_point(self):
        sol = Solution()
        points = [[0, 0], [1, 1], [2, 2]]
        k = 1
        result = sol.kClosest(points, k)
        assert result == [[0, 0]]

    def test_negative_coordinates(self):
        sol = Solution()
        points = [[-1, -1], [-2, -2], [1, 1]]
        k = 2
        result = sol.kClosest(points, k)
        assert len(result) == 2

