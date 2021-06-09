# https://leetcode.com/problems/valid-parentheses/
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        brackets = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0 or brackets[stack.pop()] != c:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()

    assert sol.isValid(s="()[]{}")
    assert not sol.isValid(s="([)]")
