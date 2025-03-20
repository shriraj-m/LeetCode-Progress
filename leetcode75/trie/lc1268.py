"""1268. Search Suggestion Systems"""

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children: 
                node.children[c] = TrieNode()
            node = node.children[c] 
            if node.n < 3:
                node.words.append(word)
                node.n += 1
        
    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: 
                return ''
            node = node.children[c] 
        return node.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for word in products:
            trie.add_word(word)
        ans = []
        cur = ''
        for c in searchWord:
            cur += c
            ans.append(trie.find_word_by_prefix(cur))
        return ans