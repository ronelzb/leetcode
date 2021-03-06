# https://leetcode.com/problems/implement-trie-prefix-tree/
# tags: #amazon, #trie, #weigthed_tree
#
# Trie implementation:
# Insert: will recursively drill down the trie for each letter in the visited word, those letter not found
# will create a new key in the visited node
# Search: Will attempt to drill down the trie until it finds the end of the word
# Starts With: As opposite to search, this method will attempt to drill down until the end of the word queried
#
# Time complexity: O(n * m) n=word length - m=lookup nodes
# Space complexity O(k * n) k=each node size - n=keys or nodes
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                return False

        return current.end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return False

        return True


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    print(t.search("apple"))  # return True
    print(t.search("app"))  # return False
    print(t.startsWith("app"))  # return True
    t.insert("app")
    print(t.search("app"))  # return True
