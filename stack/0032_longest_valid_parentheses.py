# https://leetcode.com/problems/longest-valid-parentheses/
# tags: #dp, #stack, #string
#
# Solution 1: Stack
# Instead of classical push/pop elements in the stack, let's do it for the last seen opening parentheses
# When a closing parentheses is found pop last pushed element in the stack and 2 options can happen:
# 1. If the stack is empty append current letter to the stack
# 2. If it contains data check if the current i - last seen opening parentheses is the longest
#
# Solution 2: Dynamic Programming
# If s[i] is '(', set dp[i] to 0, because any string end with '(' cannot be a valid one.
# Else if s[i] is ')'
#   If s[i-1] is '(', dp[i] = dp[i-2] + 2
#   Else if s[i-1] is ')' and s[i-dp[i-1]-1] == '(', dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
# For example, input "()(())", at i = 5, longest array is [0,2,0,0,2,0], dp[5] = dp[1] + dp[4] + 2 = 6.
# Time Complexity: O(n), Space complexity: O(n)
from collections import deque


class Solution:
    def longestValidParentheses_stack(self, s: str) -> int:
        stack = deque([-1])
        longest = 0

        for i, c in enumerate(s):
            if c == "(": stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest

    def longestValidParentheses_dp(self, s: str) -> int:
        s = ")" + s
        n = len(s)
        dp = [0] * n
        longest = 0

        for i in range(1, n):
            if s[i] == "(":
                dp[i] = 0
            elif i > 1 and s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2
                longest = max(longest, dp[i])
            elif i > dp[i - 1] + 1 and s[i - dp[i - 1] - 1] == "(":
                dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
                longest = max(longest, dp[i])

        return longest


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses_dp(s="(()"))  # 2
    print(sol.longestValidParentheses_dp(s="()(())"))  # 6
    print(sol.longestValidParentheses_dp(s=")()())"))  # 4
