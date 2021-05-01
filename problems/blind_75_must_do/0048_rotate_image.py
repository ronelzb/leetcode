from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - 1 - i):  # (i, n - i):
                # print(">>>>>>>>>", i, j)
                # upper-left temp
                temp = matrix[i][j]
                # print(temp)

                # lower-left -> upper-left
                # print(matrix[n - 1 - j][i])
                matrix[i][j] = matrix[n - 1 - j][i]
                # lower-right -> lower-left
                # print(matrix[n - 1 - i][n - 1 - j])
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # upper-right -> lower-right
                # print(matrix[j][n - 1 - i])
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # temp -> upper-right
                matrix[j][n - 1 - i] = temp


if __name__ == "__main__":
    sol = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix)
    print(matrix)
