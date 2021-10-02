# https://leetcode.com/problems/dungeon-game/
# tags: #array, #dp, #matrix
#
# Solution: Dynamic Programming
# Use dp[i][j] to store the min dp needed at position (i, j), then do the calculation from right-bottom to left-up
# Dummy row and column added to dp is used to make the code cleaner
# Time Complexity: O(m*n) => m=n => O(n^2), Space complexity: O(n^2)
import sys
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[sys.maxsize] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])

        return dp[0][0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.calculateMinimumHP(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  # 7
