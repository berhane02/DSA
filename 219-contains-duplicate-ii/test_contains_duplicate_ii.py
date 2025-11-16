import pytest
from contains_duplicate_ii import Solution

class TestContainsNearbyDuplicate:
    def test_example1(self):
        sol = Solution()
        assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) == True

    def test_example2(self):
        sol = Solution()
        assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) == True

    def test_example3(self):
        sol = Solution()
        assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False

    def test_no_duplicates(self):
        sol = Solution()
        assert sol.containsNearbyDuplicate([1, 2, 3, 4], 3) == False

    def test_duplicate_outside_window(self):
        sol = Solution()
        assert sol.containsNearbyDuplicate([1, 2, 3, 1], 2) == False

    def test_single_element(self):
        sol = Solution()
        assert sol.containsNearbyDuplicate([1], 1) == False

    def test_k_equals_zero(self):
        sol = Solution()
        assert sol.containsNearbyDuplicate([1, 2, 3, 1], 0) == False

    def test_adjacent_duplicates(self):
        sol = Solution()
        assert sol.containsNearbyDuplicate([1, 1, 2, 3], 1) == True

    def test_large_k(self):
        sol = Solution()
        assert sol.containsNearbyDuplicate([1, 2, 3, 1], 10) == True

