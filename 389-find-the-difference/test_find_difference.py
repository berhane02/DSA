import pytest
from find_the_difference import Solution

class TestFindTheDifference:
    def test_example1(self):
        sol = Solution()
        assert sol.findTheDifference("abcd", "abcde") == "e"

    def test_example2(self):
        sol = Solution()
        assert sol.findTheDifference("", "y") == "y"

    def test_difference_in_middle(self):
        sol = Solution()
        result = sol.findTheDifference("abc", "abxc")
        assert result == "x"

    def test_difference_at_start(self):
        sol = Solution()
        result = sol.findTheDifference("abc", "xabc")
        assert result == "x"

    def test_difference_at_end(self):
        sol = Solution()
        assert sol.findTheDifference("abc", "abcx") == "x"

    def test_repeated_characters(self):
        sol = Solution()
        result = sol.findTheDifference("aabbcc", "aabbccd")
        assert result == "d"

    def test_single_character(self):
        sol = Solution()
        assert sol.findTheDifference("a", "aa") == "a"

    def test_empty_first_string(self):
        sol = Solution()
        assert sol.findTheDifference("", "a") == "a"

