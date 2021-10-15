# https://leetcode.com/problems/minimum-path-sum/
# tags: #array, #dp, #matrix
#
# Solution: DP in-place
# Suppose the minimum path sum of arriving at point (i, j) is S[i][j],
# then the state equation is S[i][j] = min(S[i - 1][j], S[i][j - 1]) + grid[i][j].
# Time Complexity: O(m*n), Space complexity: O(1)
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
    print(sol.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))  # 12
    print(sol.minPathSum(grid=[[1, 2], [1, 1]]))  # 3
