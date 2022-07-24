# https://leetcode.com/problems/maximum-number-of-visible-points/
# tags: #geometry, #google, #math, #matrix, #sliding_window, #sorting
#
# Solution: Sliding Window
# * Convert all coordinates to radians array
# * Sort the array
# * As we need to go around a circle, we duplicate the array and offset to the second half by 2 * PI
# * Use sliding window to find the longest window that satisfies r_point[r] - r_points[i] <= angle
# Time complexity: O(n*log(n)), Space complexity O(n)
import math
from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        r_points = []
        points_at_location = 0
        dx, dy = location

        for x, y in points:
            if [x, y] == location:
                points_at_location += 1
                continue
            r_points.append(math.atan2(y - dy, x - dx))

        r_points.sort()
        r_points.extend([x + 2.0 * math.pi for x in r_points])
        angle = math.pi * angle / 180

        res, l = 0, 0
        for r in range(len(r_points)):
            while r_points[r] - r_points[l] > angle:
                l += 1
            res = max(res, r - l + 1)

        return res + points_at_location


if __name__ == '__main__':
    sol = Solution()
    print(sol.visiblePoints(points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]))  # 3
    print(sol.visiblePoints(points=[[1, 0], [2, 1]], angle=13, location=[1, 1]))  # 1
