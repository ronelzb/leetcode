# https://leetcode.com/problems/set-matrix-zeroes/
# tags: #array, #matrix
#
# Solution: Save states in-place
# Store state of each row-column related to (i, j) == 0 with an "x" or any nomenclature you see fit, the important
# thing here is to be consistent.
# Then make a second-pass in the matrix to find any "x" stored and swap it into a 0.
# Time complexity: O(m*n), Space complexity: O(1)
from typing import List


class Solution:
    def markColumnAndRow(self, matrix: List[List[int]], m: int, n: int, i: int, j) -> None:
        for k in range(m):
            if matrix[k][j] != 0:
                matrix[k][j] = "x"

        for l in range(n):
            if matrix[i][l] != 0:
                matrix[i][l] = "x"

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.markColumnAndRow(matrix, m, n, i, j)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "x":
                    matrix[i][j] = 0


if __name__ == "__main__":
    sol = Solution()
    sol.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])  # [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
