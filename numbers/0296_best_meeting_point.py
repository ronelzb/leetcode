# https://leetcode.com/problems/best-meeting-point/
# tags: #google, #math, #matrix
# Manhattan distance: (p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|
# The optimal point is the mean
# For example, 1-1-0-0-1, the optimal point is at x = 1, and assume the total distance is d
# If we move the point to the right, x = 2, the total distance will be d + 2 - 1,
# since there will be two points on its left and 1 point on its right
# Time complexity: O(m * n + nlog(n)), Space complexity: O(m + n)
from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols, count_ones = [], [], 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count_ones += 1
                    rows.append(i)
                    cols.append(j)

        cols.sort()
        return self.calculate_distance(rows) + self.calculate_distance(cols)

    def calculate_distance(self, points: List[int]) -> int:
        reference = points[len(points) // 2]
        return sum([abs(x - reference) for x in points])


if __name__ == "__main__":
    sol = Solution()

    print(sol.minTotalDistance(grid=[[1, 0, 0, 0, 1],
                                     [0, 0, 0, 0, 0],
                                     [0, 0, 1, 0, 0]]))  # 6

    print(sol.minTotalDistance(grid=[[1, 0, 1, 0, 1],
                                     [0, 1, 0, 0, 0],
                                     [0, 1, 1, 0, 0]]))  # 11
