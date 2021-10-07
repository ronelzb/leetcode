# https://leetcode.com/problems/n-queens-ii/
# tags: #backtracking, #dfs
#
# Solution: Backtracking
# Same solution as 51. N-Queens using backtracking
# This time I applied the following optimization:
# Whenever a location (x, y) is occupied, any other locations (p, q)
# where p + q == x + y or p - q == x - y would be invalid.
# We can use this information to keep track of the indicators (xy_dif and xy_sum)
# of the invalid positions and then call DFS recursively with valid positions only.
# Time Complexity: O(n*n!), Space complexity: O(n!)
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtracking(row: int, vert: set, xy_dif: set, xy_sum: set) -> int:
            if row == n:
                return 1

            count = 0
            for i in range(n):
                if i not in vert and row - i not in xy_dif and row + i not in xy_sum:
                    count += backtracking(row + 1, vert | {i}, xy_dif | {row - i}, xy_sum | {row + i})

            return count

        return backtracking(0, set(), set(), set())


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalNQueens(n=4))  # 2
