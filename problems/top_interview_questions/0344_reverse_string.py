# https://leetcode.com/problems/reverse-string/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i]


if __name__ == "__main__":
    sol = Solution()

    print(sol.reverseString(s=["h", "e", "l", "l", "o"]))  # ["o", "l", "l", "e", "h"]
