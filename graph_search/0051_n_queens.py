# https://leetcode.com/problems/n-queens/
# tags: #array, #backtracking
#
# Solution: Backtracking
# Use the DFS helper function to find solutions recursively.
# A solution will be found when the length of queens is equal to n (queens is a list of the indices of the queens).
# Queens stores those used cols, for example, we can check previous vertical and diagonal used cols
# Time Complexity: O(n*n!), Space complexity: O(n)
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(row: int, weave: List[str], visited: set) -> None:
            if row == n:
                combinations.append(weave)
                return

            new_weave = ["."] * n
            for col in range(n):
                valid = True
                for prev_row in range(row - 1, -1, -1):
                    left_diag = col - (row - prev_row)
                    right_diag = col + (row - prev_row)
                    if (prev_row, col) in visited \
                            or (left_diag >= 0 and (prev_row, left_diag) in visited) \
                            or (right_diag < n and (prev_row, right_diag) in visited):
                        valid = False
                        break
                if not valid: continue

                new_weave[col] = "Q"
                backtracking(row + 1, weave + ["".join(new_weave)], visited | {(row, col)})
                new_weave[col] = "."

        combinations = []
        backtracking(0, [], set())
        return combinations


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(n=1))  # [["Q"]]
    print(sol.solveNQueens(n=4))  # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
