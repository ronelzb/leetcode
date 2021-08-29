# https://leetcode.com/problems/search-a-2d-matrix-ii/
# tags: #array, #divide_and_conquer, #matrix
#
# To keep logic conditions simple, we start search from top right corner.
# If the target is greater than the value in the current position,
# then the target can not be in entire row of current position because the row is sorted.
# If the target is less than the value in the current position,
# then the target can not in the entire column because the column is also sorted.
#
# Divide and conquer explanation:
# https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66147/*Java*-an-easy-to-understand-divide-and-conquer-method
#
# Time complexity: O(m + n), Space complexity: O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:  # matrix[i][j] < target
                i += 1

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix(
        matrix=[[1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]],
        target=5)
    )  # True

    print(sol.searchMatrix(
        matrix=[[1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]],
        target=20)
    )  # False

    print(sol.searchMatrix(matrix=[[5], [6]], target=6))  # True

    print(sol.searchMatrix(
        matrix=[[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]],
        target=19)
    )  # True
