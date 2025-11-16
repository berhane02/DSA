import pytest
from sum_of_unique_elements import Solution

class TestSumOfUnique:
    def test_example1(self):
        sol = Solution()
        assert sol.sumOfUnique([1, 2, 3, 2]) == 4

    def test_example2(self):
        sol = Solution()
        assert sol.sumOfUnique([1, 1, 1, 1, 1]) == 0

    def test_example3(self):
        sol = Solution()
        assert sol.sumOfUnique([1, 2, 3, 4, 5]) == 15

    def test_all_unique(self):
        sol = Solution()
        assert sol.sumOfUnique([1, 2, 3]) == 6

    def test_all_duplicates(self):
        sol = Solution()
        assert sol.sumOfUnique([5, 5, 5]) == 0

    def test_single_element(self):
        sol = Solution()
        assert sol.sumOfUnique([10]) == 10

    def test_mixed(self):
        sol = Solution()
        assert sol.sumOfUnique([1, 2, 2, 3, 3, 4]) == 5  # 1 + 4 = 5

    def test_empty_list(self):
        sol = Solution()
        assert sol.sumOfUnique([]) == 0

