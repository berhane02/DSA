import pytest
from implement_trie_prefix_tree import Trie

class TestTrie:
    def test_example1(self):
        trie = Trie()
        trie.insert("apple")
        assert trie.search("apple") == True
        assert trie.search("app") == False
        assert trie.startsWith("app") == True
        trie.insert("app")
        assert trie.search("app") == True

    def test_empty_trie(self):
        trie = Trie()
        assert trie.search("") == False
        assert trie.startsWith("") == True

    def test_insert_and_search(self):
        trie = Trie()
        trie.insert("hello")
        assert trie.search("hello") == True
        assert trie.search("hell") == False
        assert trie.search("helloworld") == False

    def test_prefix_search(self):
        trie = Trie()
        trie.insert("hello")
        assert trie.startsWith("h") == True
        assert trie.startsWith("he") == True
        assert trie.startsWith("hel") == True
        assert trie.startsWith("hello") == True
        assert trie.startsWith("helloworld") == False

    def test_multiple_inserts(self):
        trie = Trie()
        trie.insert("cat")
        trie.insert("car")
        trie.insert("dog")
        assert trie.search("cat") == True
        assert trie.search("car") == True
        assert trie.search("dog") == True
        assert trie.search("ca") == False
        assert trie.startsWith("ca") == True

    def test_overlapping_words(self):
        trie = Trie()
        trie.insert("app")
        trie.insert("apple")
        assert trie.search("app") == True
        assert trie.search("apple") == True

