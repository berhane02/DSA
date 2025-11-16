import pytest
from subarrays_with_k_different_integers import Solution

class TestSubarraysWithKDistinct:
    def test_example1(self):
        sol = Solution()
        assert sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7

    def test_example2(self):
        sol = Solution()
        assert sol.subarraysWithKDistinct([1, 2, 1, 3, 4], 3) == 3

    def test_k_equals_one(self):
        sol = Solution()
        assert sol.subarraysWithKDistinct([1, 1, 1], 1) == 3

    def test_all_same_elements(self):
        sol = Solution()
        assert sol.subarraysWithKDistinct([1, 1, 1, 1], 1) == 10

    def test_all_different(self):
        sol = Solution()
        assert sol.subarraysWithKDistinct([1, 2, 3], 3) == 1

    def test_single_element(self):
        sol = Solution()
        assert sol.subarraysWithKDistinct([1], 1) == 1

    def test_k_greater_than_distinct(self):
        sol = Solution()
        assert sol.subarraysWithKDistinct([1, 2], 3) == 0

    def test_complex_case(self):
        sol = Solution()
        result = sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2)
        assert result == 7

