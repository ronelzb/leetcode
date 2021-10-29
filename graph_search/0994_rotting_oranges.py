# https://leetcode.com/problems/rotting-oranges/
# tags: #bfs, #google, #matrix
#
# Solution 1: Breadth-first search
# Pre-populate a queue storing the rotten oranges and count the fresh ones traversing the grid
# If there are rotten oranges in the queue and there are still fresh oranges in the grid:
# * Update the number of minutes passed
# * Process rotten oranges on the current level
# Return the number of minutes taken to make all the fresh oranges to be rotten
# Time Complexity: O(m*n), Space complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        rotten = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        minutes = 0
        while rotten and fresh_count > 0:
            minutes += 1

            for _ in range(len(rotten)):
                i, j = rotten.popleft()

                for di, dj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if m > di >= 0 and n > dj >= 0 and grid[di][dj] == 1:
                        grid[di][dj] = 2
                        rotten.append((di, dj))
                        fresh_count -= 1

        return minutes if fresh_count == 0 else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
    print(sol.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
