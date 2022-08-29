# https://leetcode.com/problems/minimum-area-rectangle/submissions/
# tags: #geometry, #google, #hash_table, #math, #sorting
# Group the points by x coordinates, so that we have columns of points.
# Then, for every pair of points in a column (with coordinates (x,y1) and (x,y2)),
# check for the smallest rectangle with this pair of points
# Time complexity: O(n^2), Space complexity: O(n)

import sys
from collections import defaultdict
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = defaultdict(set)
        for x, y in points:
            columns[x].add(y)

        min_area = sys.maxsize

        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i+1:]:
                if x1 != x2 and y1 != y2 and y2 in columns[x1] and y1 in columns[x2]:
                    min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))
                    if min_area == 1:
                        return 1

        return min_area if min_area < sys.maxsize else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.minAreaRect(points=[[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))  # 4
