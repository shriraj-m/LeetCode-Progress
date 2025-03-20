"""208. Implement Trie (Prefix Tree)"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        current_node = self.trie
        for char in word:
            # if character doesnt exist, add it to trienode()
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            
            current_node = current_node.children[char]
        current_node.is_end = True

    def search(self, word: str) -> bool:
        current_node = self.trie

        for char in word:
            if char not in current_node.children:
                return False # doesnt exist
            current_node = current_node.children[char]
        return current_node.is_end


    def startsWith(self, prefix: str) -> bool:
        current_node = self.trie
        for char in prefix:
            if char not in current_node.children:
                return False # if char not in children
            current_node = current_node.children[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)