# No link
# tags: #amazon, #trie, #weigthed_tree
#
# Make a data structure to insert new words with its weight
# and get the sum of any prefix asked
# insert("apple", 3)
# insert("ap", 2)
# sum("ap") == 5
#
# Time complexity: O(n * m) n=word length - m=lookup nodes
# Space complexity O(k * n) k=each node size - n=keys or nodes
class TrieNode:
    def __init__(self, weight):
        self.weight = weight
        self.children = dict()


def insert(word: str, weight: int, root: TrieNode) -> None:
    for c in word:
        if c not in root.children:
            root.children[c] = TrieNode(weight)
        else:
            root.children[c].weight += weight

        root = root.children[c]


def prefix_sum(prefix: str, root: TrieNode) -> int:
    for c in prefix:
        if c not in root.children:
            return -1
        else:
            root = root.children[c]

    return root.weight


def print_trie(root: TrieNode, level) -> None:
    indent = " " * level * 2
    print(indent, root.weight)
    for key, value in root.children.items():
        print(indent, key)
        print_trie(value, level + 1)


if __name__ == "__main__":
    trie_root = TrieNode(-1)
    insert("apple", 3, trie_root)
    insert("ap", 2, trie_root)
    print(prefix_sum("ap", trie_root))
    print(prefix_sum("mistake", trie_root))
