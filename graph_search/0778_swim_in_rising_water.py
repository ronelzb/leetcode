# https://leetcode.com/problems/swim-in-rising-water/
# tags: #bfs, #binary_search, #dfs, #google, #heap, #matrix, #union-find
#
# Solution 1: Dijkstra (weighted bfs) using heap
# Start with (0,0) corner, on each moment of time we choose a neighbor node with the smallest value to visit.
# In this way when we reached (n-1, n-1) corner, the answer will be the maximum of visited cells so far.
# Time complexity: O(n^2*log(n)), Space complexity: O(n^2)
import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, res = len(grid), 0
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}

        for i in range(n * n):
            val, x, y = heapq.heappop(heap)
            res = max(res, val)

            if x == n - 1 and y == n - 1:
                return res

            for dx, dy in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= dx < n and 0 <= dy < n and (dx, dy) not in visited:
                    heapq.heappush(heap, (grid[dx][dy], dx, dy))
                    visited.add((dx, dy))

        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.swimInWater(grid=[[0, 1, 2, 3, 4],
                                [24, 23, 22, 21, 5],
                                [12, 13, 14, 15, 16],
                                [11, 17, 18, 19, 20],
                                [10, 9, 8, 7, 6]]))  # 16
