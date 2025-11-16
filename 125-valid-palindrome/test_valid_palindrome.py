import pytest
from valid_palindrome import Solution

class TestIsPalindrome:
    def test_example1(self):
        sol = Solution()
        assert sol.isPalindrome("A man, a plan, a canal: Panama") == True

    def test_example2(self):
        sol = Solution()
        assert sol.isPalindrome("race a car") == False

    def test_example3(self):
        sol = Solution()
        assert sol.isPalindrome(" ") == True

    def test_simple_palindrome(self):
        sol = Solution()
        assert sol.isPalindrome("racecar") == True

    def test_not_palindrome(self):
        sol = Solution()
        assert sol.isPalindrome("hello") == False

    def test_with_numbers(self):
        sol = Solution()
        assert sol.isPalindrome("A1b2b1A") == True

    def test_empty_string(self):
        sol = Solution()
        assert sol.isPalindrome("") == True

    def test_single_character(self):
        sol = Solution()
        assert sol.isPalindrome("a") == True

    def test_only_non_alphanumeric(self):
        sol = Solution()
        assert sol.isPalindrome(".,") == True

    def test_mixed_case(self):
        sol = Solution()
        assert sol.isPalindrome("Madam") == True

