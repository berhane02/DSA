import pytest
from check_if_the_sentence_is_pangram import Solution

class TestCheckIfPangram:
    def test_example1(self):
        sol = Solution()
        assert sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") == True

    def test_example2(self):
        sol = Solution()
        assert sol.checkIfPangram("leetcode") == False

    def test_all_letters(self):
        sol = Solution()
        assert sol.checkIfPangram("abcdefghijklmnopqrstuvwxyz") == True

    def test_mixed_case(self):
        sol = Solution()
        assert sol.checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog") == True

    def test_missing_one_letter(self):
        sol = Solution()
        assert sol.checkIfPangram("abcdefghijklmnopqrstuvwxy") == False

    def test_empty_string(self):
        sol = Solution()
        assert sol.checkIfPangram("") == False

    def test_single_letter(self):
        sol = Solution()
        assert sol.checkIfPangram("a") == False

    def test_repeated_letters(self):
        sol = Solution()
        assert sol.checkIfPangram("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True

