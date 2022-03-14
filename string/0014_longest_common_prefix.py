# https://leetcode.com/problems/longest-common-prefix/
# tags: #string, #top_interview_questions
#
# Solution: Vertical scanning
# Time Complexity: O(n*m) m=min of strings, Space complexity: O(m)
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s, i, n, min_string_length = "", 0, len(strs), len(min(strs, key=len))

        while i < min_string_length:
            for j in range(1, n):
                if strs[j][i] != strs[j - 1][i]:
                    return s
            s += strs[0][i]
            i += 1

        return s


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(strs=["flower", "flow", "flight"]))  # "fl"
    print(sol.longestCommonPrefix(strs=["dog", "racecar", "car"]))  # ""
