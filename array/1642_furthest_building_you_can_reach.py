# https://leetcode.com/problems/furthest-building-you-can-reach/
# tags: #array, #greedy, #heap
#
# Solution: Heap + Greedy
# Use a min-heap to store each climb (difference) between two contiguous buildings
# Ladders for the longest jumps and the bricks for the shortest ones
# If ladders are all in used, find the current shortest climb to use bricks instead
# Time complexity: O(n*log(n)), Space complexity: O(n)
import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        min_heap = []

        for i in range(n - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue

            heapq.heappush(min_heap, climb)

            if len(min_heap) > ladders:
                bricks -= heapq.heappop(min_heap)

            if bricks < 0:
                return i

        return n - 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))  # 4
    print(sol.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))  # 7
    print(sol.furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0))  # 3
