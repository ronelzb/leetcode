# https://leetcode.com/problems/valid-parentheses/
# tags: #stack, #string, #top_interview_questions
#
# Solution: Stack
# Basic usage for stack implementation, also added bracket's dictionary to maintain the code clean
# Time complexity: O(n), Space complexity: O(n)
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        brackets = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in ("(", "{", "["):
                stack.append(c)
            else:
                if not stack or brackets[stack.pop()] != c:
                    return False

        return not stack


if __name__ == "__main__":
    sol = Solution()

    assert sol.isValid(s="()[]{}")
    assert not sol.isValid(s="([)]")
