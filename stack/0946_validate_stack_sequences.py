# https://leetcode.com/problems/validate-stack-sequences/
# tags: #array, #simulation, #stack, #two_pointers
#
# Solution: Two pointers
# Emulate all push and pop operations using the actual stack keeping tracked of pushed and popped pointers.
# Time complexity: O(n), Space complexity O(n)
from collections import deque
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j, n = 0, 0, len(pushed)
        stack = deque()

        while i < n or j < n:
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            elif i < n:
                stack.append(pushed[i])
                i += 1
            else:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))  # True
    print(sol.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))  # False
