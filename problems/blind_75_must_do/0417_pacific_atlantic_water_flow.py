# https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(i: int, j: int, visited: set, debug: bool = False) -> None:
            visited.add((i, j))

            for k, l in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= k < m and 0 <= l < n and (k, l) not in visited and heights[k][l] >= heights[i][j]:
                    dfs(k, l, visited, debug)

        pacific, atlantic = set(), set()
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)

        return list(pacific & atlantic)


if __name__ == "__main__":
    sol = Solution()

    print(sol.pacificAtlantic(
        heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    ))  # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
