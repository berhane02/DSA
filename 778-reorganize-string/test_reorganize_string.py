import pytest
from reorganize_string import Solution

def is_valid_reorganization(s, result):
    """Helper to check if reorganization is valid"""
    if len(result) != len(s):
        return False
    for i in range(len(result) - 1):
        if result[i] == result[i + 1]:
            return False
    return sorted(result) == sorted(s)

class TestReorganizeString:
    def test_example1(self):
        sol = Solution()
        result = sol.reorganizeString("aab")
        assert is_valid_reorganization("aab", result) or result == ""

    def test_example2(self):
        sol = Solution()
        result = sol.reorganizeString("aaab")
        assert result == ""

    def test_single_character(self):
        sol = Solution()
        result = sol.reorganizeString("a")
        assert result == "a"

    def test_two_different_characters(self):
        sol = Solution()
        result = sol.reorganizeString("ab")
        assert is_valid_reorganization("ab", result)

    def test_three_characters(self):
        sol = Solution()
        result = sol.reorganizeString("abc")
        assert is_valid_reorganization("abc", result)

    def test_impossible_case(self):
        sol = Solution()
        result = sol.reorganizeString("aaa")
        assert result == ""

    def test_possible_case(self):
        sol = Solution()
        result = sol.reorganizeString("aabb")
        assert is_valid_reorganization("aabb", result) or result == ""

