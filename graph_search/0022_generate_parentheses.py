# https://leetcode.com/problems/generate-parentheses/
# tags: #backtracking, #dp, #string
#
# Idea: https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution
# The goal is to print a string of “(“ ,”)” in certain order. The length of string is 2n.
# The constraints are that “(“s need to match “)”s.
# Without constraints, we just simply print out “(“ or “)” until length hits n.
# So the base case will be length ==2 n, recursive case is print out “(“ and “)”
# We need to interpret the meanings of constraints.
# First, the first character should be “(“.
# Second, at each step, you can either print “(“ or “)”, but print “)” only when there are more “(“s than “)”s.
# Stop printing out “(“ when the number of “(“ s hit n
#
#
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []

        def backtracking(weave, start, end) -> None:
            if start == n and end == n:
                parentheses.append(weave)
                return

            if start < n:
                backtracking(weave + "(", start + 1, end)
            if end < start:
                backtracking(weave + ")", start, end + 1)

        backtracking("", 0, 0)
        return parentheses


if __name__ == "__main__":
    sol = Solution()

    assert sol.generateParenthesis(n=3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
