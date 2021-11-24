# https://leetcode.com/problems/interval-list-intersections/
# tags: #array, #microsoft, #two_pointers
#
# Solution: Two pointers
# Take two pointers i, j for each list starting from 0.
# At each index find the intersection between i, j which starts at the max between them and ends at the min.
# The intersection will be added to result if start <= end.
# Use end pointer to find which index (i, j) will be moved next
# Time complexity: O(min(m, n)), Space complexity O(n)
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []

        res = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            start, end = max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])
            if start <= end: res.append([start, end])
            if end == firstList[i][1]: i += 1
            elif end == secondList[j][1]: j += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                   secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))
    # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

    print(sol.intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[]))  # []
    print(sol.intervalIntersection(firstList=[], secondList=[[4, 8], [10, 12]]))  # []
    print(sol.intervalIntersection(firstList=[[1, 7]], secondList=[[3, 10]]))  # [[3,7]]
