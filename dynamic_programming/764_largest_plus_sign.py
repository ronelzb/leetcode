# https://leetcode.com/problems/largest-plus-sign/
# tags: #array, #dp
#
# Great explanation at:
# https://leetcode.com/problems/largest-plus-sign/discuss/1453636/Intuitiveor-Explained-with-image-or-Short-and-Clean-or-C%2B%2B
#
# Another explanation:
# https://leetcode.com/problems/largest-plus-sign/discuss/113314/JavaC++Python-O(N2)-solution-using-only-one-grid-matrix/114381
#
# For each position (i, j) of the grid matrix, we try to extend in each of the four directions (left, right, up, down)
# as long as possible:
# 1. For the left direction, i is a row index while j is a column index.
# For each row, j goes from left to right (increasing).
# 2. For the right direction, i is a row index while k is a column index.
# For each row, k goes from right to left (decreasing).
# 3. For the up direction, i is a column index while j is a row index.
# For each column, j goes from top to bottom (increasing).
# 4. For the down direction, i is a column index while k is a row index.
# For each column, k goes from bottom to top (decreasing).
#
# Time Complexity: O(n^2), Space complexity: O(n^2)
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        matrix = [[n] * n for _ in range(n)]
        for mine in mines:
            matrix[mine[0]][mine[1]] = 0

        for i in range(n):
            left, right, top, bottom = 0, 0, 0, 0

            for j, k in zip(range(n), reversed(range(n))):
                left = left + 1 if matrix[i][j] > 0 else 0
                if left < matrix[i][j]:
                    matrix[i][j] = left

                right = right + 1 if matrix[i][k] > 0 else 0
                if right < matrix[i][k]:
                    matrix[i][k] = right

                top = top + 1 if matrix[j][i] > 0 else 0
                if top < matrix[j][i]:
                    matrix[j][i] = top

                bottom = bottom + 1 if matrix[k][i] > 0 else 0
                if bottom < matrix[k][i]:
                    matrix[k][i] = bottom

        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, matrix[i][j])

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.orderOfLargestPlusSign(n=5, mines=[[4, 2]]))  # 2
