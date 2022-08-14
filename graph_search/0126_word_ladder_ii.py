# https://leetcode.com/problems/word-ladder-ii/
# tags: #backtracking, #bfs, #graph_search
#
# Solution: Bidirectional BFS + backtracking
# Variation problem of [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
# In this solution we will store the current word as the key in a dictionary will all the possible sequences
# to get to it.
# https://leetcode.com/problems/word-ladder-ii/discuss/269012/Python-BFS%2BBacktrack-Greatly-Improved-by-bi-directional-BFS
# UPDATE: This solution needs improvement as the tests got more strict, and it's resulting in TLE
# Time complexity: O(b^(d/2)) => b = branch factor, d = depth
# Space complexity: O(V*E)
from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        path = defaultdict(set)
        n = len(beginWord)
        distinct_chars_in_words = {c for word in wordList for c in word}

        found, rev = False, False
        begin_queue, end_queue, next_queue = {beginWord}, {endWord}, set()

        while begin_queue and not found:
            wordList -= begin_queue

            for word in begin_queue:
                for new_word in [word[:i] + c + word[i + 1:] for i in range(n) for c in distinct_chars_in_words]:
                    if new_word in wordList:
                        if new_word in end_queue:
                            found = True
                        else:
                            next_queue.add(new_word)
                        path[new_word].add(word) if rev else path[word].add(new_word)
            begin_queue, next_queue = next_queue, set()
            if len(begin_queue) > len(end_queue):
                begin_queue, end_queue, rev = end_queue, begin_queue, not rev

        # backtracking (DFS) for solution
        def backtrack(word):
            return [[word]] if word == endWord else [[word] + rest for y in path[word] for rest in backtrack(y)]
        return backtrack(beginWord)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
    # [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]

    print(sol.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
    # []
