# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# tags: #array, #greedy, #sorting
#
# Solution: Greedy
# * Sort the segments by each second item of the points, that will be the segment end.
# * Traverse the array checking if the start of the next segment is beyond our current end.
# Time complexity: O(n*log(n)), Space complexity O(1)
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        num_arrows, pivot = 0, None
        points.sort(key=lambda x: x[1])

        for start, end in points:
            if pivot is None or start > pivot:
                num_arrows += 1
                pivot = end

        return num_arrows


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2
    print(sol.findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))  # 4
    print(sol.findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))  # 2

    print(sol.findMinArrowShots(
        points=[[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]))  # 2
