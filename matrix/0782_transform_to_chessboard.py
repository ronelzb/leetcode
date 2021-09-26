# https://leetcode.com/problems/transform-to-chessboard/
# tags: #array, #bit_manipulation, #math, #matrix
#
# Solution explanation at:
# https://leetcode.com/problems/transform-to-chessboard/discuss/114847/C%2B%2BJavaPython-Solution-with-Explanation
#
# Solution: Bit manipulation
# * Intuition: Any rectangle inside the board with corners top left, top right, bottom left, bottom right
# must be 4 zeros or 2 ones 2 zeros or 4 zeros, to prove this we use XOR, which is commutative and associative.
# * Count the sum of rows/cols sum and misplacement elements, we'll use them later
# * Checking the first row and column is sufficient, because the top left corner rectangle is verified
# * When n is odd, only one final pattern is possible, the actual count of misplaced elements is 2 == n - misplaced
# * When n is even, then the final pattern is the inverse of "1010...", i.e. "0101...",
# we can pick the minimum of misplaced and (n - misplaced) to treat them as even
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(n) for j in range(n)): return -1

        row_sum, rows_misplaced, col_sum, cols_misplaced = 0, 0, 0, 0
        for i in range(n):
            row_sum += board[0][i]
            col_sum += board[i][0]

            if board[i][0] == i % 2: rows_misplaced += 1
            if board[0][i] == i % 2: cols_misplaced += 1

        if not n // 2 <= row_sum <= (n + 1) // 2: return -1
        if not n // 2 <= col_sum <= (n + 1) // 2: return -1

        if n % 2 == 1:
            if rows_misplaced % 2 == 1: rows_misplaced = n - rows_misplaced
            if cols_misplaced % 2 == 1: cols_misplaced = n - cols_misplaced
        else:
            rows_misplaced = min(rows_misplaced, n - rows_misplaced)
            cols_misplaced = min(cols_misplaced, n - cols_misplaced)

        return (cols_misplaced + rows_misplaced) // 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.movesToChessboard(board=[[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]))  # 2
    print(sol.movesToChessboard(board=[[1, 0], [0, 1]]))  # 0
    print(sol.movesToChessboard(board=[[1, 1, 0], [0, 0, 1], [0, 0, 1]]))  # 2
