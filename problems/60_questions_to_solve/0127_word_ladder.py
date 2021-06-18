# https://leetcode.com/problems/word-ladder/
from collections import deque
from typing import List


class Solution:
    # Idea: Use BFS in a graph-type search to find the shortest path
    # At first, we'll use a queue like we normally do in a BFS
    # Then, for each node (evaluated word) let's look for a neighbor which has an adjacency
    # Adjacency: Will have a most one char difference
    # if a neighbor word is found remove it from the original set to skip visit it again (undirected graph)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        char_set = {c for word in wordList for c in word}
        queue = deque([(1, beginWord)])
        n = len(beginWord)

        while queue:
            path_sum, node = queue.popleft()
            if node == endWord:
                return path_sum

            for i in range(n):
                for c in char_set:
                    if c != node[i]:
                        next_word = node[:i] + c + node[i + 1:]
                        if next_word in word_set:
                            word_set.remove(next_word)
                            queue.append((path_sum + 1, next_word))

        return 0


if __name__ == "__main__":
    sol = Solution()

    print(sol.ladderLength(beginWord="hit", endWord="cog", wordList=["hit", "hot", "dot", "dog", "lot", "log", "cog"]))  # 5
