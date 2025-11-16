import pytest
from longest_palindromic_subsequence import Solution

class TestLongestPalindromeSubseq:
    def test_example1(self):
        sol = Solution()
        assert sol.longestPalindromeSubseq("bbbab") == 4

    def test_example2(self):
        sol = Solution()
        assert sol.longestPalindromeSubseq("cbbd") == 2

    def test_single_character(self):
        sol = Solution()
        assert sol.longestPalindromeSubseq("a") == 1

    def test_all_same_characters(self):
        sol = Solution()
        assert sol.longestPalindromeSubseq("aaaa") == 4

    def test_no_palindrome(self):
        sol = Solution()
        assert sol.longestPalindromeSubseq("abc") == 1

    def test_perfect_palindrome(self):
        sol = Solution()
        assert sol.longestPalindromeSubseq("racecar") == 7

    def test_two_characters(self):
        sol = Solution()
        assert sol.longestPalindromeSubseq("ab") == 1
        assert sol.longestPalindromeSubseq("aa") == 2

    def test_complex_case(self):
        sol = Solution()
        result = sol.longestPalindromeSubseq("abcdef")
        assert result >= 1

