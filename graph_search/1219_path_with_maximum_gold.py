# https://leetcode.com/problems/path-with-maximum-gold/
# tags: #backtracking, #dfs, #google, #matrix

# Solution: DFS
# Classical dfs solution where we traverse the matrix finding the max path score
# At each dfs call we tag the current (x, y) as seen to avoid cycles and
# find the max path in all four directions (up, down, left, right)
# Time complexity: O(k*4^k + m*n - k), Space complexity: O(m*n)
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int, seen: set) -> int:
            current = grid[x][y]
            seen.add((x, y))
            max_path = 0

            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] and (dx, dy) not in seen:
                    max_path = max(max_path, dfs(dx, dy, seen))

            seen.remove((x, y))
            return current + max_path

        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    max_gold = max(max_gold, dfs(i, j, set()))
        return max_gold


if __name__ == '__main__':
    sol = Solution()
    print(sol.getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]))  # 24
    print(sol.getMaximumGold(grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))  # 28
