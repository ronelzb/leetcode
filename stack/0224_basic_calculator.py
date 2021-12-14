# https://leetcode.com/problems/basic-calculator/
# tags: #facebook, #matrix, #recursion, #stack, #string
#
# Solution: Sign stack + Two Pointers
# In order to solve this problem in one-pass do the following:
# 1. When the current char is numeric find the move i to the next non-numeric char or end of the string
# and add this found number along with the last sign found.
# 2. Else, we have two options:
#    * If the current char is a closing parenthesis just remove the last seen sign.
#    * This is the tricky part, if the current char is a minus '-' append an inverted sign to the stack, on the
#      contrary if it's a plus or an opening parenthesis append the last seen sign to the stack consistent and
#      move the index.
# Time complexity: O(n), Space complexity O(n)
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        i, n, total,  = 0, len(s), 0
        signs = deque([1, 1])

        while i < n:
            c = s[i]

            if c.isdigit():
                start = i
                while i < n and s[i].isdigit():
                    i += 1
                total += int(s[start: i]) * signs.pop()
            else:
                if s[i] == ")":
                    signs.pop()
                elif s[i] in '+-(':
                    signs.append(signs[-1] * (1, -1)[c == "-"])
                i += 1

        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate(s="1 + 1"))  # 2
    print(sol.calculate(s=" 2-1 + 2 "))  # 3
    print(sol.calculate(s="(1+(4+5+2)-3)+(6+8)"))  # 23
