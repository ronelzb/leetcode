# https://leetcode.com/problems/cherry-pickup-ii/
# tags: #dp, #matrix
#
# Solution: DFS + Dynamic Programming
# @hiepit solution
# Let dp(r, c1, c2) is the maximum cherries we can collect in grid from row=r to bottom row,
# where c1 is the column position of robot1, c2 is the column position of robot2.
# At each step, we move both robot1 and robot2 to next row, and with all possibles columns (c-1, c, c+1).
# If both robots access the same cell, we can only collect cherries once.
# Time complexity: O(9*m*n^2)=> O(m*n^2), Space complexity O(m*n^2)
from functools import lru_cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(row: int, robot1: int, robot2: int):
            if row == m: return 0
            cherries = grid[row][robot1] if robot1 == robot2 else grid[row][robot1] + grid[row][robot2]
            max_collected = 0

            for n_pos_robot1 in range(robot1 - 1, robot1 + 2):
                for n_pos_robot2 in range(robot2 - 1, robot2 + 2):
                    if 0 <= n_pos_robot1 < n and 0 <= n_pos_robot2 < n:
                        max_collected = max(max_collected, dfs(row + 1, n_pos_robot1, n_pos_robot2))

            return max_collected + cherries

        return dfs(0, 0, n - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.cherryPickup(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))  # 24
    print(sol.cherryPickup(
        grid=[[1, 0, 0, 0, 0, 0, 1],
              [2, 0, 0, 0, 0, 3, 0],
              [2, 0, 9, 0, 0, 0, 0],
              [0, 3, 0, 5, 4, 0, 0],
              [1, 0, 2, 3, 0, 0, 6]]))  # 28
