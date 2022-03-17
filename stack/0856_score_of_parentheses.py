# https://leetcode.com/problems/score-of-parentheses/
# tags: #stack
#
# Solution: Stack
# When we see "(" character, we are entering new valid parenthesis, so we append initialized value 0 to stack.
# When we see ")" character, we should process currently open valid parenthesis Stack.pop().
# If valid parenthesis score is still valued 0, it is a valid empty parenthesis, so value is 1.
# Otherwise, multiply inside value by 2. Add processed value to outer valid parenthesis stack[-1]
# Time complexity: O(n), Space complexity O(n)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                last_value = stack.pop()
                score = 1 if last_value == 0 else last_value * 2
                stack[-1] += score

        return stack[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.scoreOfParentheses(s="()"))  # 1
    print(sol.scoreOfParentheses(s="(())"))  # 2
    print(sol.scoreOfParentheses(s="()()"))  # 2
