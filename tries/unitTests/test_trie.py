# test_trie.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"), "Error: search('apple')")
        self.assertFalse(self.trie.search("app"), "Error: search('app')")
        self.assertTrue(self.trie.startsWith("app"), "Error: startsWith('app')")
        
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"), "Error: search('app') after insert('app')")
    
    def test_additional_cases(self):
        self.trie.insert("banana")
        self.assertTrue(self.trie.search("banana"), "Error: search('banana')")
        self.assertFalse(self.trie.search("ban"), "Error: search('ban')")
        self.assertTrue(self.trie.startsWith("ban"), "Error: startsWith('ban')")
        
        self.trie.insert("band")
        self.assertTrue(self.trie.search("band"), "Error: search('band')")
        self.assertFalse(self.trie.startsWith("banda"), "Error: startsWith('banda')")
        
        self.trie.insert("bandana")
        self.assertTrue(self.trie.search("bandana"), "Error: search('bandana')")
    
if __name__ == "__main__":
    unittest.main()
