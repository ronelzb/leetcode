# https://leetcode.com/problems/maximal-square/
# tags: #array, #dp
#
# Solution 1: Stack columns
# Solution to problem 85 maximal rectangle using a stack to keep track of the last column visited
# height[col] >= height[stack[-1]] is used to only consider those heights less than the height's stored in the stack.
# The while loop will create the condition where height's store in the stack is always in ascending order
# towards the top of the stack
# * height[stack.pop()] is guaranteed to be the limiting height due to the stack ascending order nature
# Time complexity: O(m*n), Space complexity: O(n)
#
# Solution 2: Dynamic Programming
# * Create a dp grid with initial values of 0.
# * Whenever we see a "1" in the matrix we will look for its surrounding elements,
# if the surrounding element it's a 1 then increase the square size.
# Time complexity: O(m*n), Space complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cols = len(matrix[0])
        height = [0] * (cols + 1)
        largest_square = 0

        for row in matrix:
            for col in range(cols):
                height[col] = height[col] + 1 if row[col] == "1" else 0
            stack = deque([-1])

            for col in range(cols + 1):
                while height[col] < height[stack[-1]]:

                    h = height[stack.pop()]
                    w = col - 1 - stack[-1]
                    largest_square = max(largest_square, min(h, w) ** 2)
                stack.append(col)

        return largest_square

    def maximalSquare_dp(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        largest_square = 0

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    dp[row + 1][col + 1] = min(dp[row][col], dp[row + 1][col], dp[row][col + 1]) + 1
                    largest_square = max(largest_square, dp[row + 1][col + 1])

        return largest_square ** 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximalSquare_dp(matrix=[["1", "0", "1", "0", "0"],
                                    ["1", "0", "1", "1", "1"],
                                    ["1", "1", "1", "1", "1"],
                                    ["1", "0", "0", "1", "0"]]))  # 4
