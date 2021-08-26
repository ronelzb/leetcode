# https://leetcode.com/problems/word-ladder/
# tags: #bfs, #google, #graph_search
# Idea: Use BFS in a graph-type search to find the shortest path
# At first, we'll use a queue like we normally do in a BFS
# Then, for each node (evaluated word) let's look for a neighbor which has an adjacency
# Adjacency: Will have a most one char difference
# if a neighbor word is found remove it from the original set to skip visit it again (undirected graph)
# Time complexity: O(n * c * l) => n = len(word), c = distinct chars in wordList, l = len(wordList)
# Space complexity: O(c + l + q) => 2 different sets plus the queue
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        distinct_words = set(wordList)
        distinct_chars_in_words = {c for word in wordList for c in word}
        queue = deque([(1, beginWord)])
        n = len(beginWord)

        while queue:
            path_sum, node = queue.popleft()
            if node == endWord:
                return path_sum

            for i in range(n):
                for c in distinct_chars_in_words:
                    next_word = node[:i] + c + node[i + 1:]
                    if next_word in distinct_words:
                        distinct_words.remove(next_word)
                        queue.append((path_sum + 1, next_word))

        return 0


if __name__ == "__main__":
    sol = Solution()

    print(sol.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
