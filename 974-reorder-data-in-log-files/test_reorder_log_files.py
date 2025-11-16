import pytest
from reorder_data_in_log_files import Solution

class TestReorderLogFiles:
    def test_example1(self):
        sol = Solution()
        logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        result = sol.reorderLogFiles(logs)
        expected = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
        assert result == expected

    def test_example2(self):
        sol = Solution()
        logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
        result = sol.reorderLogFiles(logs)
        expected = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
        assert result == expected

    def test_only_letter_logs(self):
        sol = Solution()
        logs = ["let1 art can", "let2 own kit dig"]
        result = sol.reorderLogFiles(logs)
        expected = ["let1 art can", "let2 own kit dig"]
        assert result == expected

    def test_only_digit_logs(self):
        sol = Solution()
        logs = ["dig1 8 1 5 1", "dig2 3 6"]
        result = sol.reorderLogFiles(logs)
        expected = ["dig1 8 1 5 1", "dig2 3 6"]
        assert result == expected

    def test_single_log(self):
        sol = Solution()
        logs = ["let1 art can"]
        result = sol.reorderLogFiles(logs)
        assert result == ["let1 art can"]

    def test_tie_breaking(self):
        sol = Solution()
        logs = ["let1 art can", "let2 art can", "dig1 1 2 3"]
        result = sol.reorderLogFiles(logs)
        # When content is same, should sort by identifier
        assert result[0].startswith("let1")
        assert result[1].startswith("let2")

