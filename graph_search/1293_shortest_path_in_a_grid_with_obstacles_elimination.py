# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# tags: #array, #bfs, #matrix
#
# Solution: Breadth-First Search
# * We are trying to find the shortest path thus we use BFS to exit immediately when a path reaches the
# bottom right most cell.
# * In this problem, besides visited(x, y) we need to add 1 more param k, which is the number of obstacles
# we can eliminate when we start at cell (x, y)
# Time Complexity: O(m*n*k), Space complexity: O(m*n*k)
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0, k)])
        visited = set()

        while queue:
            x, y, steps, remaining = queue.popleft()
            if (x, y) == (m - 1, n - 1):
                return steps

            visited.add((x, y, remaining))
            for i, j in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= i < m and 0 <= j < n and (grid[i][j] == 0 or remaining > 0):
                    new_remaining = remaining - grid[i][j]

                    if (i, j, new_remaining) not in visited:
                        visited.add((i, j, new_remaining))
                        queue.append((i, j, steps + 1, new_remaining))

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPath(grid=
                           [[0, 0, 0],
                            [1, 1, 0],
                            [0, 0, 0],
                            [0, 1, 1],
                            [0, 0, 0]],
                           k=1))  # 6

    print(sol.shortestPath(grid=
                           [[0, 1, 1],
                            [1, 1, 1],
                            [1, 0, 0]],
                           k=1))  # -1

    print(sol.shortestPath(grid=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ], k=1))  # 20
