# https://leetcode.com/problems/maximum-number-of-points-with-cost/
# tags: #array, #dp
#
# Solution:
# We first go left-to-right, and track the running maximum value (run_max).
# For each step, we decrement it to account for the distance, and compare with the value right above.
# Then, we do the same right-to-left, and add the maximum of two running values to each cell.
# https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/Python-3-DP-Explanation-with-pictures
# Problem similar to:
# * [931. Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/)
# * [1014. Best sightseeing pair](https://leetcode.com/problems/best-sightseeing-pair/)
# Time complexity: O(m*n), Space complexity O(n)
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        for i in range(m - 1):
            for j in range(n - 2, -1, -1):
                points[i][j] = max(points[i][j], points[i][j + 1] - 1)

            for j in range(n):
                points[i][j] = max(points[i][j], points[i][j - 1] - 1 if j > 0 else 0)
                points[i + 1][j] += points[i][j]

        return max(points[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxPoints(points=[[1, 2, 3], [1, 5, 1], [3, 1, 1]]))  # 9
    print(sol.maxPoints(points=[[1, 5], [2, 3], [4, 2]]))  # 11
