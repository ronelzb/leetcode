from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        equivalence = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")" or c == "}" or c == "]":
                if not stack or stack.pop() != equivalence[c]:
                    return False

        return True if not stack else False


if __name__ == "__main__":
    sol = Solution()
    print("() >", sol.isValid("()"))
    print("()[]{} >", sol.isValid("()[]{}"))
    print("(] >", sol.isValid("(]"))
    print("([)] >", sol.isValid("([)]"))
    print("{[]} >", sol.isValid("{[]}"))
