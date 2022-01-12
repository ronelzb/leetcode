# https://leetcode.com/problems/basic-calculator-ii/
# tags: #facebook, #math, #stack
#
# Solution: Stack with precedence
# We will maintain two separate stacks, one to store operators' op one to store numbers nums.
# If we get a digit, we will form complete number and push it into num stack
# If we get an operator, we pop previous operators of greater or equal precedence from op stack,
# evaluate it on the top two numbers from num stack and push the result back into num stack.
# Finally, we push the current operator into op for later evaluation.
# Time complexity: O(n), Space complexity O(1) each stack will never grow beyond 3 elements
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        def precedence(c: str) -> int:
            if c == "/" or c == "*": return 1
            else: return 0

        current = 0
        op, nums = deque(), deque()

        for c in s + "$":
            if c == " ": continue
            elif c.isdigit():
                current = current * 10 + int(c)
            else:
                nums.append(current)
                while op and precedence(c) <= precedence(op[-1]):
                    num2, num1, current_oper = nums.pop(), nums.pop(), op.pop()
                    if current_oper == "/": nums.append(num1 // num2)
                    elif current_oper == "*": nums.append(num1 * num2)
                    elif current_oper == "+": nums.append(num1 + num2)
                    elif current_oper == "-": nums.append(num1 - num2)
                op.append(c)
                current = 0

        return nums.pop()


if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate(s="3+2*2"))  # 7
    print(sol.calculate(s=" 3+5 / 2 "))  # 5
    print(sol.calculate(s="1+2*5/3+6/4*2"))  # 6
