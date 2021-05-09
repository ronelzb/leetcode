# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
    def __init__(self):
        self.board = None
        self.word = None
        self.m = None
        self.n = None
        self.word_length = None

    def _exist(self, i, j, k, visited) -> bool:
        if self.board[i][j] != self.word[k]:
            return False

        if k == self.word_length - 1:
            return True

        if i > 0 and (i - 1, j) not in visited:
            if self._exist(i - 1, j, k + 1, visited | {(i, j)}):
                return True
        if i < self.m - 1 and (i + 1, j) not in visited:
            if self._exist(i + 1, j, k + 1, visited | {(i, j)}):
                return True
        if j > 0 and (i, j - 1) not in visited:
            if self._exist(i, j - 1, k + 1, visited | {(i, j)}):
                return True
        if j < self.n - 1 and (i, j + 1) not in visited:
            if self._exist(i, j + 1, k + 1, visited | {(i, j)}):
                return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.m, self.n, self.word_length = len(board), len(board[0]), len(word)

        for i in range(self.m):
            for j in range(self.n):
                if self._exist(i, j, 0, set()):
                    return True

        return False


if __name__ == "__main__":
    sol = Solution()
    # assert sol.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
    print(sol.exist(board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], word="ABCESEEEFS"))
