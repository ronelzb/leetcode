# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# tags: #stack, #string
#
# Solution: Stack
# In this solution is required to make two passes:
# 1. Identify all indexes that should be removed.
# 2. Build a new string with removed indexes.
# This approach uses a stack in the first pass to store all those indexes with parentheses malformed
# Then, in the second pass we can either remove the indexes found or build the new string skipping indexes in the stack.
# Time complexity: O(n), Space complexity: O(n)
from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()

        for i, c in enumerate(s):
            if c == "(" or (c == ")" and (not stack or stack[-1][0] != "(")):
                stack.append((c, i))
            elif c == ")" and stack:
                stack.pop()

        list_s = list(s)
        while stack:
            list_s.pop(stack.pop()[1])

        return "".join(list_s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minRemoveToMakeValid(s="lee(t(c)o)de)"))  # "lee(t(c)o)de" | "lee(t(co)de)" | "lee(t(c)ode)"
    print(sol.minRemoveToMakeValid(s="a)b(c)d"))  # "ab(c)d"
    print(sol.minRemoveToMakeValid(s="))(("))  # ""
