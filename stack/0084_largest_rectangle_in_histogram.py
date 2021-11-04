# https://leetcode.com/problems/largest-rectangle-in-histogram/
# tags: #array, #stack
#
# Solution: Monotonic Stack
# For index current, we can expand the area to both the left and right, as long as heights[current]
# is the minimal height in the rectangle.
# In other words, we need to find the sub array that has the maximal widths and heights[current]
# is the minimal value of the sub array.
#
# We can use a monotonic stack to achieve this goal:
# when a pop() occurs, height[current] is the right boundary of stack.peek().
# after the pop(), stack.peek() becomes the left boundary of the previous peek element.
# Time complexity: O(n^2), Space complexity O(n)
from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        heights = [0] + heights + [0]
        res = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                current = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[current])
            stack.append(i)

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))  # 10
    print(sol.largestRectangleArea(heights=[2, 4]))  # 4
