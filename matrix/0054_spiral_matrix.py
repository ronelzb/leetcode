# https://leetcode.com/problems/spiral-matrix/
# tags: #array, #matrix
#
# Nice explanation:
# https://leetcode.com/problems/spiral-matrix/discuss/801834/Python-O(m*n)-by-simulation-w-Visualization
#
# Solution: Layer by Layer
# Traverse right increasing top, down decreasing right, left decreasing bottom and finally up increasing left
# taking special consideration in which direction we're going so to use the for loop adequately.
# Time complexity: O(n * m), Space complexity: O(n * m)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        result = []

        while top <= bottom and left <= right:
            result.extend(matrix[top][x] for x in range(left, right + 1))
            top += 1

            result.extend(matrix[y][right] for y in range(top, bottom + 1))
            right -= 1

            result.extend(matrix[bottom][x] for x in range(right, left - 1, -1) if bottom >= top)
            bottom -= 1

            result.extend(matrix[y][left] for y in range(bottom, top - 1, -1) if right >= left)
            left += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert sol.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6,
                                                                                     7]
    assert sol.spiralOrder(matrix=[[7], [9], [6]]) == [7, 9, 6]
