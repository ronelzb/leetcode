# https://leetcode.com/problems/game-of-life/
from typing import List


class Solution:
    # Ideas: The first and foremost challenge is to make the updates in-place and there some data structures to
    # achieve it: storing it in a hashtable, has the original matrix kept but all those will result in space O(n)
    # What we can do in O(1) space is to store an additional bit to the left so we keep the original state as is
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                count = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if 0 <= k < m and 0 <= l < n and (k, l) != (i, j) and board[k][l] & 1:
                            count += 1

                if (board[i][j] & 1 and 2 <= count <= 3) or count == 3:
                    board[i][j] |= 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


if __name__ == "__main__":
    sol = Solution()

    b = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol.gameOfLife(b)
    assert b == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
