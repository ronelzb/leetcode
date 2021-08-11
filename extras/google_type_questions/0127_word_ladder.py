# https://leetcode.com/problems/word-ladder/
from collections import deque
from typing import List


class Solution:
    # Same solution as 60_questions_to_solve\0127_word_ladder.py
    # Time complexity: O(n * c * l) => n = len(word), c = distinct chars in wordList, l = len(wordList)
    # Space complexity: O(c + l + q) => 2 different sets plus the queue
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
