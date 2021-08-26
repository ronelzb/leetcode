# https://leetcode.com/problems/maximal-rectangle/
# tags: #array, #dp, #google, #matrix, #stack
#
# Great explanation at:
# https://leetcode.com/problems/maximal-rectangle/discuss/29065/AC-Python-DP-solutioin-120ms-based-on-largest-rectangle-in-histogram
# The solution is based on the
# largest rectangle in histogram solution (https://leetcode.com/problems/largest-rectangle-in-histogram/)
# * We loop from 0 to n + 1 because we are considering a height array with a zero at the end (edge case)
# * We add a zero at the end to make sure to condition in which the current considered height is less than
# the height's stored in the stack.
# * The while loop is the inverse of: If we run height[i] >= height[stack[-1]] keep stacking
# * Also, the while loop will create the condition where height's store in the stack is always in ascending order
# towards the top of the stack
# * height[stack.pop()] is guaranteed to be the limiting height due to the stack ascending order nature
# * w = i - 1 - stack[-1], (i - 1) represents the right boundary of the rectangle and stack[-1] is the left
#
# Time complexity: O(m * n), Space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0

        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = deque([-1])

            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)

        return ans


if __name__ == "__main__":
    sol = Solution()

    print(sol.maximalRectangle(matrix=[["1", "0", "1", "0", "0"],
                                       ["1", "0", "1", "1", "1"],
                                       ["1", "1", "1", "1", "1"],
                                       ["1", "0", "0", "1", "0"]]))  # 6

    print(sol.maximalRectangle(matrix=[["0", "1"], ["1", "0"]]))  # 1
