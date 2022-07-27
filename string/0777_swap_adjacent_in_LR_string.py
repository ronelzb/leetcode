# https://leetcode.com/problems/swap-adjacent-in-lr-string/
# tags: #google, #string, #two_pointers
#
# Solution 1: Two pointers
# Based on the problem's contraints we need to check the following:
# * If the current character is L, the index in start must be greater the index in end
# * If the current character is R, the index in start must be less the index in end
# Time complexity: O(n), Space complexity O(1)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j, n = 0, 0, len(start)

        while i < n or j < n:
            while i < n and start[i] == "X":
                i += 1
            while j < n and end[j] == "X":
                j += 1

            if i == n or j == n:
                return i == j

            if start[i] != end[j] or (start[i] == "L" and i < j) or (start[i] == "R" and i > j):
                return False

            i += 1
            j += 1

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canTransform(start="RXXLRXRXL", end="XRLXXRRLX"))  # True
    print(sol.canTransform(start="XXXLRXRXL", end="XRLXXRRLX"))  # False
    print(sol.canTransform(start="X", end="L"))  # False
    print(sol.canTransform(start="LR", end="RL"))  # False
    print(sol.canTransform(start="LXXLXRLXXL", end="XLLXRXLXLX"))  # False
    print(sol.canTransform(start="RXR", end="XXR"))  # False
