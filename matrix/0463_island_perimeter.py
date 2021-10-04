# https://leetcode.com/problems/island-perimeter/
# tags: #array, #dfs, #matrix
#
# Solution 1: Simple counting
# Time Complexity: O(m*n), Space complexity: O(1)
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                        if x < 0 or x > m - 1 or y < 0 or y > n - 1 or grid[x][y] == 0:
                            perimeter += 1

        return perimeter


if __name__ == "__main__":
    sol = Solution()
    print(sol.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))  # 16
