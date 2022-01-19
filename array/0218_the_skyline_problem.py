# https://leetcode.com/problems/the-skyline-problem/
# tags: #array, #binary_indexed_tree, #divide_and_conquer, #heap, #line_sweep, #ordered_set, #segment_tree
#
# Solution 1: Sweep line using Ordered set + Heap
# pos will store all coordinates where the largest height may change
# active stores all buildings ranging the current coordinate
# The push(-height, end) will store all buildings in ascending order into the heap
# At each iteration, active must have the current tallest building for the current position
# Time complexity: O(n*log(n)), Space complexity O(n)
import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        pos = sorted(set([b[0] for b in buildings] + [b[1] for b in buildings]))
        idx, prev_height = 0, 0
        active, result = [], []

        for curr_pos in pos:
            while active and active[0][1] <= curr_pos:
                heapq.heappop(active)

            while idx < n and buildings[idx][0] <= curr_pos:
                heapq.heappush(active, (-buildings[idx][2], buildings[idx][1]))
                idx += 1

            if active:
                curr_height = -active[0][0]
                if curr_height != prev_height:
                    result.append([curr_pos, curr_height])
                    prev_height = curr_height
            else:
                result.append([curr_pos, 0])
                prev_height = -1

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    # [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

    print(sol.getSkyline(buildings=[[1, 3, 3], [2, 4, 4], [5, 8, 2], [6, 7, 4], [8, 9, 4]]))
    # [[1,3],[2,4],[4,0],[5,2],[6,4],[7,2],[8,4],[9,0]]
