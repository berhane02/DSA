import pytest
from contains_duplicate import Solution

class TestContainsDuplicate:
    def test_example1(self):
        sol = Solution()
        assert sol.containsDuplicate([1, 2, 3, 1]) == True

    def test_example2(self):
        sol = Solution()
        assert sol.containsDuplicate([1, 2, 3, 4]) == False

    def test_example3(self):
        sol = Solution()
        assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

    def test_empty_array(self):
        sol = Solution()
        assert sol.containsDuplicate([]) == False

    def test_single_element(self):
        sol = Solution()
        assert sol.containsDuplicate([1]) == False

    def test_two_same_elements(self):
        sol = Solution()
        assert sol.containsDuplicate([1, 1]) == True

    def test_two_different_elements(self):
        sol = Solution()
        assert sol.containsDuplicate([1, 2]) == False

    def test_duplicate_at_end(self):
        sol = Solution()
        assert sol.containsDuplicate([1, 2, 3, 4, 5, 1]) == True

    def test_duplicate_at_start(self):
        sol = Solution()
        assert sol.containsDuplicate([1, 1, 2, 3, 4]) == True

    def test_all_same_elements(self):
        sol = Solution()
        assert sol.containsDuplicate([5, 5, 5, 5]) == True

