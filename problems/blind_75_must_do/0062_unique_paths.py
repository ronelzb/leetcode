# https://leetcode.com/problems/unique-paths/
class Solution:
    def __init__(self):
        self.visited = dict()

    def uniquePaths(self, m: int, n: int, i: int = 0, j: int = 0) -> int:
        if i == m - 1 and j == n - 1:
            return 1
        if (i, j) in self.visited:
            return self.visited[(i, j)]

        paths = 0
        if i < m - 1:
            paths += self.uniquePaths(m, n, i + 1, j)
        if j < n - 1:
            paths += self.uniquePaths(m, n, i, j + 1)

        self.visited[(i, j)] = paths
        return paths

    def uniquePathsDP(self, m: int, n: int):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = [[0] * n for _ in range(m)]
        for i in range(n):
            table[0][i] = 1
        for j in range(m):
            table[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i - 1][j] + table[i][j - 1]
        return table[m - 1][n - 1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.uniquePathsDP(m=3, n=2) == 3
    # assert sol.uniquePaths(m=7, n=3) == 28
    # assert sol.uniquePaths(m=3, n=3) == 6
    # assert sol.uniquePaths(m=1, n=3) == 1
    assert sol.uniquePathsDP(m=22, n=13) == 354817320
