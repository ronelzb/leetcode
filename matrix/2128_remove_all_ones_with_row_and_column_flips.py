# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/
# tags: #array, #bit_manipulation, #google, #math, #matrix
#
# Solution: DFS
# Based on @leet_go comment:
# 1. Order of flips does not matter, which means that doing flip row1,
# flip col1 should be exactly the same as doing flip col1, flip row1 on a random matrix.
# The reason is that for each of the flip, we do one Not operation on each of the cell in the
# row/column and by doing a sequence of flips , the total number of Not operation on each cell
# is fixed and thus order of the flip does not make a difference.
# 2. As a result, if there is a solution that we can remove all ones, we can first do all row flips,
# then columns flips, which means that after row flips all columns should either be all zeros or all ones.
# That's why each row should have the same "pattern"
# Time complexity : O(m * n), Space complexity: O(n)
from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1, r1_flip = grid[0], [1 - val for val in grid[0]]

        for i in range(1, len(grid)):
            if grid[i] != r1 and grid[i] != r1_flip:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeOnes(grid=[[0, 1, 0], [1, 0, 1], [0, 1, 0]]))  # True
    print(sol.removeOnes(grid=[[1, 1, 0], [0, 0, 0], [0, 0, 0]]))  # False
