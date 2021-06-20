# https://leetcode.com/problems/max-area-of-island/
from typing import List


class Solution:
    # Time complexity : O(m * n)
    # Space complexity: O(L) where L is the size of the largest island, representing the max recursion stack
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = float("-inf")
        m, n = len(grid), len(grid[0])

        def get_area(i: int, j: int) -> int:
            area = 1
            grid[i][j] = 0
            for k, l in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= k < m and 0 <= l < n and grid[k][l] == 1:
                    area += get_area(k, l)

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, get_area(i, j))

        return max_area if max_area > float("-inf") else 0


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxAreaOfIsland(grid=[
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]) == 6

    assert sol.maxAreaOfIsland(grid=[[1]]) == 1
