# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=211548593612944&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time Complexity: O(n), Space complexity: O(n)
from collections import deque


class Solution:
    def isBalanced(self, s: str) -> bool:
        stack = deque()
        brackets = {"{": "}", "[": "]", "(": ")"}

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack or brackets[stack[-1]] != c: return False
                stack.pop()
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isBalanced("{[()]}"))  # True
    print(sol.isBalanced("{}()"))  # True
    print(sol.isBalanced("{(})"))  # False
    print(sol.isBalanced(")"))  # False
