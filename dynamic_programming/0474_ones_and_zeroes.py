# https://leetcode.com/problems/unique-paths-ii/
# tags: #dp, #string
#
# Solution: Dynamic Programming
# This problem is a variation of the Knapsack Problem with a twist: each item has a 2-dimensional weight,
# but a constant value.
# For our dp grid, dp[i][j] will represent the largest number of items that can be added to yield i zeros and j ones.
# Thus, our answer will ultimately be dp[M][N]
# Time complexity: O(L*m*n), Space complexity: O(m*n)
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeroes = s.count("0")
            ones = len(s) - zeroes
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroes][j - ones] + 1)

        return dp[m][n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))  # 4
