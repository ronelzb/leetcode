# https://leetcode.com/problems/surrounded-regions/
# tags: #array, #bfs, #dfs, #matrix, #union-find
#
# Solution: Depth-first Search
# Start from the boundaries, and use DFS (or BFS) to flip the 'O's that are connected to the edge by another
# character different than X or O, spread the symbol to all connected 'O's horizontally or vertically.
# Eventually, change back all "*" back to O which are the result of all connected edges.
# Time complexity: O(m*n), Space complexity O(1)
from itertools import product
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(x: int, y: int) -> None:
            if m > x >= 0 and n > y >= 0 and board[x][y] == "O":
                board[x][y] = "*"
                for dx, dy in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    dfs(dx, dy)

        m, n = len(board), len(board[0])
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        for i, j in product(range(m), range(n)):
            board[i][j] = "X" if board[i][j] != "*" else "O"

        return None


if __name__ == "__main__":
    sol = Solution()

    grid = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    sol.solve(board=grid)
    print(grid)  # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
