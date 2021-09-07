# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# tags: #array, #math, #stack
#
# Classical stack problem: Traverse the list storing each number found in the stack, when an operator is found
# pop the latest 2 values stored and make the proper operator upon them being careful of the division operation
# if the result number is less than zero we need to store the ceiling. Eventually store the result back into the
# stack.
# for the case 1/-22, python returns -1, so its recommended to use itruediv to get a float then apply int() to get 0
#
# Time Complexity: O(n), Space complexity: O(n)
import operator
from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.itruediv}

        for token in tokens:
            if token in operators:
                second, first = stack.pop(), stack.pop()
                stack.append(int(operators[token](first, second)))
            else:
                stack.append(int(token))

        return stack.pop()


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(tokens=["2", "1", "+", "3", "*"]))  # 9
    print(sol.evalRPN(tokens=["4", "13", "5", "/", "+"]))  # 6
    print(sol.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
