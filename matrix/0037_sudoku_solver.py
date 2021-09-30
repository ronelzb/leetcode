# https://leetcode.com/problems/sudoku-solver/
# tags: #array, #backtracking, #google, #matrix
#
# Solution: Backtracking
# DSF turn into backtracking solution, starting with row 0 we'll traverse through each row to 9 and restart
# col = 0 to thoroughly check all numbers at each recursion.
# Is valid will check if the visited number does not each in the same row/column/block.
# To backtracking we need to restore the updated board[i][j] back to "."
# Time Complexity: O(9^n) n=represents number of blanks to fill in, Space complexity: O(n)
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def backtracking(row: int) -> bool:
            for i in range(row, 9):
                col = 0
                for j in range(col, 9):
                    if board[i][j] != ".": continue
                    for num in range(9):
                        char = chr(num + 49)

                        if is_valid(i, j, char):
                            board[i][j] = char
                            if backtracking(i):
                                return True
                            board[i][j] = "."
                    return False
            return True

        def is_valid(row: int, col: int, char) -> bool:
            block_row, block_col = (row // 3) * 3, (col // 3) * 3
            for i in range(9):
                if board[row][i] == char or \
                        board[i][col] == char or \
                        board[block_row + i // 3][block_col + i % 3] == char:
                    return False
            return True

        backtracking(0)

        return None


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveSudoku(
        board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    # [["5","3","4","6","7","8","9","1","2"],
    # ["6","7","2","1","9","5","3","4","8"],
    # ["1","9","8","3","4","2","5","6","7"],
    # ["8","5","9","7","6","1","4","2","3"],
    # ["4","2","6","8","5","3","7","9","1"],
    # ["7","1","3","9","2","4","8","5","6"],
    # ["9","6","1","5","3","7","2","8","4"],
    # ["2","8","7","4","1","9","6","3","5"],
    # ["3","4","5","2","8","6","1","7","9"]]
