# https://leetcode.com/problems/search-a-2d-matrix/
# tags: #matrix
#
# Solution 1: Naive approach
# Starting from the top-right corner of the grid we can go backwards into looking up the target
# Time Complexity: O(m+n), Space complexity: O(1)
#
# Solution 2: Binary Search
# Virtual flatten this matrix into a ordered list: if we need element number i from our flattened list,
# it corresponds to element matrix[i//n][i%n] in our matrix.
# Time Complexity: O(log(m*n)) => O(log(m)+log(n)), Space complexity: O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: j -= 1
            else: i += 1
        return False

    def searchMatrix_binarySearch(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left < right:
            middle = (left + right) // 2
            if matrix[middle // n][middle % n] < target:
                left = middle + 1
            else:
                right = middle

        return matrix[left // n][left % n] == target


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix_binarySearch(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))  # True
    print(sol.searchMatrix_binarySearch(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=34))  # True
    print(sol.searchMatrix_binarySearch(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))  # False
    print(sol.searchMatrix_binarySearch(matrix=[[1, 1]], target=2))  # False
