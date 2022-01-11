# https://leetcode.com/problems/max-points-on-a-line/
# tags: #geometry, #google, #hash_table, #math
#
# Solution: Dictionary slope counter
# Given a point p, we compute the slopes of all lines connecting p and other points.
# Points corresponding to the same slope will fall on the same line.
# In this way, we can figure out the maximum number of points on lines containing p.
# We exhaust all possible p's and the largest maximum number is just the answer.
#
# To represent a slope (dy / dx), we may simply use a float value, but it won't have the precision necessary.
# Instead, we calculate the gcd between dx and dy and divide x and y by that gcd separately.
# Overlap is the same point visited.
# Time complexity: O(n^2 * log(n)) log(n)=gcd, Space complexity O(n^2)
from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a: int, b: int) -> int:
            if b == 0: return a
            return gcd(b, a % b)

        n = len(points)
        if n <= 2: return n
        max_points = 0

        for i in range(n):
            slope_counter = defaultdict(int)
            overlap = 0
            current_max = 0

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue

                current_gcd = gcd(dx, dy)
                dx //= current_gcd
                dy //= current_gcd
                slope_counter[(dx, dy)] += 1
                current_max = max(current_max, slope_counter[(dx, dy)])

            max_points = max(max_points, current_max + overlap + 1)

        return max_points


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))  # 3
    print(sol.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # 4
