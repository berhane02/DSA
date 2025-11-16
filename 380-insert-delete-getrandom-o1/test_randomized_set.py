import pytest
from insert_delete_getrandom_o1 import RandomizedSet

class TestRandomizedSet:
    def test_example1(self):
        randomizedSet = RandomizedSet()
        assert randomizedSet.insert(1) == True
        assert randomizedSet.remove(2) == False
        assert randomizedSet.insert(2) == True
        random_val = randomizedSet.getRandom()
        assert random_val in [1, 2]
        assert randomizedSet.remove(1) == True
        assert randomizedSet.insert(2) == False
        assert randomizedSet.getRandom() == 2

    def test_insert_duplicate(self):
        randomizedSet = RandomizedSet()
        assert randomizedSet.insert(1) == True
        assert randomizedSet.insert(1) == False

    def test_remove_nonexistent(self):
        randomizedSet = RandomizedSet()
        assert randomizedSet.remove(1) == False

    def test_get_random_single_element(self):
        randomizedSet = RandomizedSet()
        randomizedSet.insert(5)
        assert randomizedSet.getRandom() == 5

    def test_multiple_operations(self):
        randomizedSet = RandomizedSet()
        randomizedSet.insert(1)
        randomizedSet.insert(2)
        randomizedSet.insert(3)
        assert randomizedSet.remove(2) == True
        random_val = randomizedSet.getRandom()
        assert random_val in [1, 3]

    def test_empty_set(self):
        randomizedSet = RandomizedSet()
        # getRandom on empty set behavior depends on implementation
        # Typically should handle gracefully

