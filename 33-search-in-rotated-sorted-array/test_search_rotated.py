import pytest
from search_in_rotated_sorted_array import Solution

class TestSearch:
    def test_example1(self):
        sol = Solution()
        assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_example2(self):
        sol = Solution()
        assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_example3(self):
        sol = Solution()
        assert sol.search([1], 0) == -1

    def test_no_rotation(self):
        sol = Solution()
        assert sol.search([1, 2, 3, 4, 5], 3) == 2

    def test_target_at_pivot(self):
        sol = Solution()
        assert sol.search([4, 5, 6, 7, 0, 1, 2], 7) == 3

    def test_single_element_found(self):
        sol = Solution()
        assert sol.search([1], 1) == 0

    def test_single_element_not_found(self):
        sol = Solution()
        assert sol.search([1], 0) == -1

    def test_two_elements(self):
        sol = Solution()
        assert sol.search([1, 3], 3) == 1
        assert sol.search([3, 1], 1) == 1

    def test_target_in_left_half(self):
        sol = Solution()
        assert sol.search([4, 5, 6, 7, 0, 1, 2], 5) == 1

    def test_target_in_right_half(self):
        sol = Solution()
        assert sol.search([4, 5, 6, 7, 0, 1, 2], 1) == 5

