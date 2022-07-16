# https://leetcode.com/problems/out-of-boundary-paths/
# tags: #dp
#
# Solution: DFS + cache
# https://leetcode.com/problems/edit-distance/discuss/411610/python-dfs-cache-and-dp
# The idea here is to use brute force to take a step in every direction until we don't have
# any movements left, we count the times we move outside the boundaries of the grid
# As we have redundant dfs function calls, then we use @lru_cache decorator to
# memoize previously seen number of possible movements leading to a path out.
# Time complexity : O(m * n * maxMove), Space complexity: O(m * n * maxMove)
from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(k: int, i: int, j: int) -> int:
            if i >= m or i < 0 or j >= n or j < 0:
                return 1
            if k == 0:
                return 0

            res = 0
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                res += dfs(k - 1, x, y)
            return res

        return dfs(maxMove, startRow, startColumn) % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))  # 6
    print(sol.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))  # 12
