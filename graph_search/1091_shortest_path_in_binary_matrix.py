# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# tags: #array, #bfs
#
# Solution: Breadth-First Search
# Classical solution when finding the shortest path between 2 points, think of adjacent cells with value = 0 having an
# undirected edge between them.
# Keep a visited set to avoid traverse through a node twice.
# Time complexity: O(n^2), Space complexity: O(n^2)
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        visited = set()

        if grid[0][0] == 0: queue.append((0, 0, 1))

        while queue:
            x, y, lvl = queue.popleft()
            if x == n - 1 and y == n - 1: return lvl
            visited.add((x, y))

            for i, j in ((x + a, y + b) for a in [-1, 0, 1] for b in [-1, 0, 1]):
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 0 and (i, j) not in visited:
                    visited.add((i, j))
                    queue.append((i, j, lvl + 1))

        return -1


if __name__ == '__main__':
    sol = Solution()
    # print(sol.shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]))  # 2
    print(sol.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # 4
    # print(sol.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]]))  # -1
