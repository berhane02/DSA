import pytest
from group_anagrams import Solution

def normalize_result(result):
    """Helper to sort inner lists for comparison"""
    return sorted([sorted(group) for group in result])

class TestGroupAnagrams:
    def test_example1(self):
        sol = Solution()
        result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        normalized = normalize_result(result)
        expected = normalize_result([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
        assert normalized == expected

    def test_example2(self):
        sol = Solution()
        result = sol.groupAnagrams([""])
        assert normalize_result(result) == normalize_result([[""]])

    def test_example3(self):
        sol = Solution()
        result = sol.groupAnagrams(["a"])
        assert normalize_result(result) == normalize_result([["a"]])

    def test_no_anagrams(self):
        sol = Solution()
        result = sol.groupAnagrams(["abc", "def", "ghi"])
        normalized = normalize_result(result)
        expected = normalize_result([["abc"], ["def"], ["ghi"]])
        assert normalized == expected

    def test_all_same(self):
        sol = Solution()
        result = sol.groupAnagrams(["abc", "abc", "abc"])
        normalized = normalize_result(result)
        expected = normalize_result([["abc", "abc", "abc"]])
        assert normalized == expected

    def test_single_character_strings(self):
        sol = Solution()
        result = sol.groupAnagrams(["a", "b", "a", "b"])
        normalized = normalize_result(result)
        expected = normalize_result([["a", "a"], ["b", "b"]])
        assert normalized == expected

    def test_empty_strings(self):
        sol = Solution()
        result = sol.groupAnagrams(["", "", "a"])
        normalized = normalize_result(result)
        expected = normalize_result([["", ""], ["a"]])
        assert normalized == expected

