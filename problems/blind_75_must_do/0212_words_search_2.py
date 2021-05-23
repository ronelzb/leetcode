# https://leetcode.com/problems/word-search-ii/
from typing import List


class Solution:
    # This problem can be divided into 2 sub problems in order to efficiently solve it:
    # 1. Build a trie based on the provided words
    # 2. DFS through the entire board and in each step verify if a word was found
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        end_of_word = "#"
        found_words = set()
        trie = dict()

        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node[end_of_word] = True

        def dfs(i: int, j: int, node: dict, built_word: str) -> None:
            if board[i][j] in node:
                c = board[i][j]
                built_word += c
                node = node[c]

                if end_of_word in node:
                    found_words.add(built_word)
                    if len(node) == 1:  # if next node is empty, no need to search deeper
                        return

                board[i][j] = ""  # instead of using a visited set, we can temporarily delete the char in this pos

                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n:
                        dfs(x, y, node, built_word)

                board[i][j] = c

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie, "")

        return list(found_words)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                        words=["oath", "pea", "eat", "rain"]))
