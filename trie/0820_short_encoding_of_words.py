# https://leetcode.com/problems/short-encoding-of-words/
# tags: #array, #hash_table, #string, #trie
#
# Solution: Trie
# We can find similar suffixes by reversing each word and adding it to our trie.
# Then, we can perform DFS on the tree-like structure to obtain all maximum-length chains
# Time complexity: O(n*k) n chains of length k, Space complexity: O(n*k)
from collections import defaultdict
from typing import List


class Solution:
    END_OF_WORD = "#"

    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = dict()

        for word in words:
            current = root
            for c in word[::-1]:
                current.setdefault(c, dict())
                current = current[c]

        def dfs(node: dict, curr: int) -> int:
            return sum(dfs(adj, curr + 1) for adj in node.values()) if node else curr

        return dfs(root, 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumLengthEncoding(words=["time", "me", "bell"]))  # 10
    print(sol.minimumLengthEncoding(words=["t"]))  # 2
