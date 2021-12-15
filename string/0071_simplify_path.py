# https://leetcode.com/problems/simplify-path/
# tags: #facebook, #stack
#
# Solution: Stack
# Push to the stack every valid file name (not in {"","."})
# Pop out of the stack when ".." is met.
# Time Complexity: O(n), Space complexity: O(n)
from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        places = [p for p in path.split("/") if p != "." and p != ""]
        stack = deque()

        for p in places:
            if p == "..":
                if stack: stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath(path="/home/"))  # "/home"
    print(sol.simplifyPath(path="/../"))  # "/../"
    print(sol.simplifyPath(path="/home//foo/"))  # "/home/foo"
    print(sol.simplifyPath(path="/a/./b/../../c/"))  # "/c"
    print(sol.simplifyPath(path="/a/../../b/../c//.//"))  # "/c"
