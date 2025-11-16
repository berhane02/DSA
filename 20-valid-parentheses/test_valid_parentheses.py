import pytest
from valid_parentheses import Solution

class TestIsValid:
    def test_example1(self):
        sol = Solution()
        assert sol.isValid("()") == True

    def test_example2(self):
        sol = Solution()
        assert sol.isValid("()[]{}") == True

    def test_example3(self):
        sol = Solution()
        assert sol.isValid("(]") == False

    def test_nested_valid(self):
        sol = Solution()
        assert sol.isValid("([{}])") == True

    def test_nested_invalid(self):
        sol = Solution()
        assert sol.isValid("([)]") == False

    def test_empty_string(self):
        sol = Solution()
        assert sol.isValid("") == True

    def test_only_opening(self):
        sol = Solution()
        assert sol.isValid("(") == False
        assert sol.isValid("([{") == False

    def test_only_closing(self):
        sol = Solution()
        assert sol.isValid(")") == False
        assert sol.isValid(")]}") == False

    def test_mismatched_types(self):
        sol = Solution()
        assert sol.isValid("(}") == False
        assert sol.isValid("[)") == False
        assert sol.isValid("{]") == False

    def test_complex_valid(self):
        sol = Solution()
        assert sol.isValid("((()))") == True
        assert sol.isValid("{[()]}") == True

