# https://leetcode.com/problems/daily-temperatures/
# tags: #monotonic_stack, #stack
#
# Solution: Monotonic Stack
# We need to know the current distance from the Next Greater Number
# The for loop scans elements from the back to the front, and while we use the stack structure and
# enter the stack back to front, we are actually going to exit the stack front to back.
# The while loop is to rule out the elements between the two "tall" elements.
# Their existence has no meaning, because there is a "taller" element in front of them, and they cannot be
# considered as the distance to the Next Great Number of the subsequent elements
# Time complexity: O(n), Space complexity O(n)
from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = deque()
        days_to_wait = [0] * n

        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            days_to_wait[i] = stack[-1] - i if stack else 0
            stack.append(i)

        return days_to_wait


if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
