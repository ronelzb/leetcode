# https://leetcode.com/problems/rotate-image/
# tags: #array, #math, #matrix
#
# Solution: Transpose and reverse
# We process the outer circle of the matrix, and then we go deep to the inner circle until the side length of
# the last inner circle is smaller than 2 (meaning there is only one center element left).
# For each circle, we exchange elements clockwise and after we finish one circle,
# we can continue processing the next.
# Time complexity: O(n^2), Space complexity: O(1)
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - 1 - i):  # (i, n - i):
                # upper-left temp
                temp = matrix[i][j]
                # lower-left -> upper-left
                matrix[i][j] = matrix[n - 1 - j][i]
                # lower-right -> lower-left
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # upper-right -> lower-right
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # temp -> upper-right
                matrix[j][n - 1 - i] = temp


if __name__ == "__main__":
    sol = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix)
    print(matrix)
