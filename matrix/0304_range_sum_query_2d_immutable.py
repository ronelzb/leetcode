# https://leetcode.com/problems/range-sum-query-2d-immutable/
# tags: #design, #matrix, #prefix_sum
#
# Solution: Prefix sum
# Instead of traversing an array everytime to find the sum on O (n), we use prefix sum.
# Basically, for each row in the matrix we apply the rolling sum (adding previous col [j-1] value) to each col j.
# With this we can find sumRegion in TC O(n) just subtracting col2 - col1 values for each row
# Time complexity: O(m*n), Space complexity: O(m)
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self._prefix_rows_sum = matrix

        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self._prefix_rows_sum[i][j] += self._prefix_rows_sum[i][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0

        for i in range(row1, row2 + 1):
            res += self._prefix_rows_sum[i][col2] - (self._prefix_rows_sum[i][col1 - 1] if col1 > 0 else 0)

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
if __name__ == '__main__':
    num_matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(num_matrix.sumRegion(2, 1, 4, 3))  # 8
    print(num_matrix.sumRegion(1, 1, 2, 2))  # 11
    print(num_matrix.sumRegion(1, 2, 2, 4))  # 12
