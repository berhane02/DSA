import pytest
from longest_substring_without_repeating_characters import Solution

class TestLengthOfLongestSubstring:
    def test_example1(self):
        sol = Solution()
        assert sol.lengthOfLongestSubstring("abcabcbb") == 3

    def test_example2(self):
        sol = Solution()
        assert sol.lengthOfLongestSubstring("bbbbb") == 1

    def test_example3(self):
        sol = Solution()
        assert sol.lengthOfLongestSubstring("pwwkew") == 3

    def test_empty_string(self):
        sol = Solution()
        assert sol.lengthOfLongestSubstring("") == 0

    def test_single_character(self):
        sol = Solution()
        assert sol.lengthOfLongestSubstring("a") == 1

    def test_all_unique(self):
        sol = Solution()
        assert sol.lengthOfLongestSubstring("abcdef") == 6

    def test_repeating_at_end(self):
        sol = Solution()
        assert sol.lengthOfLongestSubstring("dvdf") == 3

    def test_space_character(self):
        sol = Solution()
        assert sol.lengthOfLongestSubstring(" ") == 1

    def test_special_characters(self):
        sol = Solution()
        assert sol.lengthOfLongestSubstring("!@#$%^&*()") == 10

