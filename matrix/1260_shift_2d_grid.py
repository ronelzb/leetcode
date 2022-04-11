# https://leetcode.com/problems/shift-2d-grid/
# tags: #array, #matrix, #simulation
#
# Solution 1: Resolve Index
# Since shifting right will put the last k cells in grid on the first k cells
# We can get the proper new number into the grid getting the corresponding cell based on k
# Time complexity: O(m*n), Space complexity O(m*n)
#
# Solution 1: Reverse
# * Reverse all elements
# * Then, first k elements, be careful with the index
# * Finally, Reverse last m * n - k elements
# Time complexity: O(m*n), Space complexity O(1)
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                index = i * cols + j + k
                res[index // cols % rows][index % cols] = grid[i][j]

        return res

    def shiftGrid_reverse(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def reverse(left, right, col):
            while left < right:
                grid[left // col][left % col], grid[right // col][right % col] = \
                    grid[right // col][right % col], grid[left // col][left % col]
                left, right = left + 1, right - 1

        rows, cols = len(grid), len(grid[0])
        length = rows * cols
        k %= length

        reverse(0, length - 1, cols)
        reverse(0, k - 1, cols)
        reverse(k, length - 1, cols)

        return grid


if __name__ == "__main__":
    sol = Solution()
    print(sol.shiftGrid_reverse(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))  # [[9,1,2],[3,4,5],[6,7,8]]
