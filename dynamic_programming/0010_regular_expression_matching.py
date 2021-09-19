# https://leetcode.com/problems/regular-expression-matching/
# tags: #dp
#
# Solution 1: Recursion
# Traverse string from left to right until pattern is empty, then check if s is empty (base condition)
# Before calling the recursion consider the edge case: when the length is greater than 2 and p[1] == "*":
# * Pattern skips two characters directly. Indicates that the character before * appears 0 times
# * Pattern remains unchanged, for example text = aa, pattern = a*, the first a matches,
# and then the second a of text matches the first a of pattern. Means * replace with the previous character
# Time Complexity: O(2^k) k=min(n, m), Space complexity: O(n+m) due to recursion calls
# Space complexity: No matter what is to happen the index of either s or p will be incremented
# in the next recursive function so the worst case of the depth will be n+m
#
# Solution 2: Dynamic Programming
# Explanation: https://www.youtube.com/watch?v=l3hda49XcDE&list=PLrmLmBdmIlpuE5GEMDXWf0PWbBD9Ga1lO
# * dp[i][j]: if s[0..i-1] matches p[0..j-1]
# * if p[j - 1] != '*'
# *     dp[i][j] = dp[i - 1][j - 1] && s[i - 1] == p[j - 1]
# * if p[j - 1] == '*', denote p[j - 2] with x
# *     dp[i][j] is true if any of the following is true
# *         1) "x*" repeats 0 time and matches empty: dp[i][j - 2]
# *         2) "x*" repeats >= 1 times and matches "x*x": s[i - 1] == x and dp[i - 1][j]
# * '.' matches any single character
# Time complexity: O(n*m), Space complexity: O(n*m)
class Solution:
    def isMatch_recursion(self, s: str, p: str) -> bool:
        if not p: return not s

        first_match = s and (s[0] == p[0] or p[0] == ".")
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch_recursion(s, p[2:]) or (first_match and self.isMatch_recursion(s[1:], p))
        else:
            return first_match and self.isMatch_recursion(s[1:], p[1:])

    def isMatch_dp(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for j in range(2, m + 1):
            dp[0][j] = p[j - 1] == "*" and dp[0][j - 2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] != "*":
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
                else:
                    dp[i][j] = dp[i][j - 2] or (s[i - 1] == p[j - 2] or p[j - 2] == ".") and dp[i - 1][j]

        return dp[n][m]


if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch_dp(s="aaa", p="a*"))  # True
    print(sol.isMatch_recursion(s="ab", p=".*"))  # True
    print(sol.isMatch_recursion(s="mississippi", p="mis*is*p*."))  # False
    print(sol.isMatch_recursion(s="mississippi", p="mis*is*ip*."))  # True
