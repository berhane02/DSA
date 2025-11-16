import pytest
from two_sum import Solution

class TestTwoSum:
    def test_example1(self):
        sol = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        result = sol.twoSum(nums, target)
        assert result == [0, 1] or result == [1, 0]
        assert nums[result[0]] + nums[result[1]] == target

    def test_example2(self):
        sol = Solution()
        nums = [3, 2, 4]
        target = 6
        result = sol.twoSum(nums, target)
        assert result == [1, 2] or result == [2, 1]
        assert nums[result[0]] + nums[result[1]] == target

    def test_example3(self):
        sol = Solution()
        nums = [3, 3]
        target = 6
        result = sol.twoSum(nums, target)
        assert result == [0, 1] or result == [1, 0]
        assert nums[result[0]] + nums[result[1]] == target

    def test_negative_numbers(self):
        sol = Solution()
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = sol.twoSum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    def test_mixed_numbers(self):
        sol = Solution()
        nums = [-1, 0, 1, 2, -1, -4]
        target = 0
        result = sol.twoSum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    def test_large_array(self):
        sol = Solution()
        nums = list(range(1000))
        target = 1998
        result = sol.twoSum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

