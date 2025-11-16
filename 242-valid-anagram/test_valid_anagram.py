import pytest
from valid_anagram import Solution

class TestIsAnagram:
    def test_example1(self):
        sol = Solution()
        assert sol.isAnagram("anagram", "nagaram") == True

    def test_example2(self):
        sol = Solution()
        assert sol.isAnagram("rat", "car") == False

    def test_same_string(self):
        sol = Solution()
        assert sol.isAnagram("abc", "abc") == True

    def test_different_lengths(self):
        sol = Solution()
        assert sol.isAnagram("abc", "abcd") == False

    def test_single_character(self):
        sol = Solution()
        assert sol.isAnagram("a", "a") == True
        assert sol.isAnagram("a", "b") == False

    def test_empty_strings(self):
        sol = Solution()
        assert sol.isAnagram("", "") == True

    def test_different_char_counts(self):
        sol = Solution()
        assert sol.isAnagram("aab", "abb") == False

    def test_anagram_with_repeats(self):
        sol = Solution()
        assert sol.isAnagram("listen", "silent") == True

    def test_not_anagram_same_chars(self):
        sol = Solution()
        assert sol.isAnagram("aacc", "ccac") == False

