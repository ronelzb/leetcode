# https://leetcode.com/discuss/interview-question/553454/facebook-phone-change-working-directory
# Solution: Stack + Working directory knowledge
# Variant of LeetCode Simplify Path (https://leetcode.com/problems/simplify-path/).
# For validation and edge case purposes: If change starts with a '/' current has to be emptied.
# From there, just concatenate current directory with change args.
# Use a stack to keep track of the last directory and where we are heading to.
# Time complexity: O(n), Space complexity O(n)
from collections import deque


class Solution:
    def constructPath(self, cwd: str, cd: str) -> str:
        if not cd:
            return cwd
        elif cd[0] == "/":
            cwd = ""

        stack = deque()
        for dir in (cwd + "/" + cd).split("/"):
            if dir == "..":
                if stack: stack.pop()
            elif dir == "." or not dir:
                continue
            else:
                stack.append(dir)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.constructPath("/", "foo"))  # "/foo"
    print(sol.constructPath("/baz", "/bar"))  # "/bar"
    print(sol.constructPath("/foo/bar", "../../../../.."))  # "/"
    print(sol.constructPath("/x/y", "../p/../q"))  # "/x/q"
    print(sol.constructPath("/x/y", "/p/./q"))  # "/p/q"
