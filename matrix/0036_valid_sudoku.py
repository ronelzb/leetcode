# https://leetcode.com/problems/valid-sudoku/
# tags: #array, #hash_table, #matrix
#
# Solution: Sets
# Save the state of each valid number visited by row/column/sub-boxes
# Time Complexity: O(n^2), Space complexity: O(3*n) => O(n)
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_rows, num_cols = set(), set()

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                rect = set()
                for x in range(3):
                    for y in range(3):
                        row, col = i + x, j + y
                        num = board[row][col]

                        if num == ".": continue

                        if num in rect or (row, num) in num_rows or (col, num) in num_cols:
                            return False

                        rect.add(num)
                        num_rows.add((row, num))
                        num_cols.add((col, num))

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidSudoku(board=
                            [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))  # True

    print(sol.isValidSudoku(board=
                            [["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))  # False

    print(sol.isValidSudoku(board=
                            [[".", ".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", ".", ".", ".", ".", ".", "."],
                             [".", "9", ".", ".", ".", ".", ".", ".", "1"],
                             ["8", ".", ".", ".", ".", ".", ".", ".", "."],
                             [".", "9", "9", "3", "5", "7", ".", ".", "."],
                             [".", ".", ".", ".", ".", ".", ".", "4", "."],
                             [".", ".", ".", "8", ".", ".", ".", ".", "."],
                             [".", "1", ".", ".", ".", ".", "4", ".", "9"],
                             [".", ".", ".", "5", ".", "4", ".", ".", "."]]))  # False
