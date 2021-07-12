# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    # Solution: Simple dfs to mark an "island" as seen to count distinct islands in the grid
    # Time complexity: O(m*n), Space complexity: O(m*n)
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            grid[i][j] = 0

            for (k, l) in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= k < m and 0 <= l < n and grid[k][l] == "1":
                    dfs(k, l)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count


if __name__ == "__main__":
    sol = Solution()

    assert sol.numIslands(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3  # 3
