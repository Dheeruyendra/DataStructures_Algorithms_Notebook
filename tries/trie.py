class TrieNode:
    def __init__(self):                  #TC=> O(1)
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):               #TC=> O(len(word))
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True          
    
    def search(self, word):                #TC=> O(len(word))
        node = self.root
        for char in word:
            if char not in node.children:
                return False 
            node = node.children[char]
        return node.word           
    
    def startsWith(self, prefix):         #TC=> O(len(prefix))
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False 
            node = node.children[char]
        return True      
                       