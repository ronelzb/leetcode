# https://leetcode.com/problems/spiral-matrix-ii/
# tags: #array, #matrix
#
# Solution: Layer by Layer
# Spiral Matrix solution variant walking the matrix from the outside to the center
# Time Complexity: O(n^2), Space complexity: O(1)
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1
        counter = 1

        while top <= bottom and left <= right:
            for x in range(left, right + 1):
                matrix[top][x] = counter
                counter += 1
            top += 1

            for y in range(top, bottom + 1):
                matrix[y][right] = counter
                counter += 1
            right -= 1

            for x in range(right, left - 1, -1):
                if bottom < top: break
                matrix[bottom][x] = counter
                counter += 1
            bottom -= 1

            for y in range(bottom, top - 1, -1):
                if right < left: break
                matrix[y][left] = counter
                counter += 1
            left += 1

        return matrix


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateMatrix(n=1))  # [[1]]
    print(sol.generateMatrix(n=2))  # [[1,2],[4,3]]
    print(sol.generateMatrix(n=3))  # [[1,2,3],[8,9,4],[7,6,5]]
