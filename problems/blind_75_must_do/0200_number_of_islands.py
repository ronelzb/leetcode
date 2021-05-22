# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        m, n = len(grid), len(grid[0])

        def dfs_island(i: int, j: int) -> None:
            grid[i][j] = "#"

            if i > 0 and grid[i - 1][j] == "1":
                dfs_island(i - 1, j)
            if i < m - 1 and grid[i + 1][j] == "1":
                dfs_island(i + 1, j)
            if j > 0 and grid[i][j - 1] == "1":
                dfs_island(i, j - 1)
            if j < n - 1 and grid[i][j + 1] == "1":
                dfs_island(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count += 1
                    dfs_island(i, j)

        return island_count


if __name__ == "__main__":
    sol = Solution()

    assert sol.numIslands(grid=[
      ["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]
    ]) == 3
