# https://leetcode.com/problems/distinct-subsequences/
# tags: #dp, #sequence, #string
#
# Good approach example and explanation:
# https://leetcode.com/problems/distinct-subsequences/discuss/37387/A-DP-solution-with-clarification-and-explanation
#
# Solution: Dynamic Programming
# * dp[j] = dp[j]            (discard s[i])
# *         + dp[i-1][j-1]   (s[i] == t[j] if they match we add the subsequence found to the cache)
# We traverse j in t to i backwards backwards so we are using dp[j-1] from last time step
# Time Complexity: O(n*m), Space complexity: O(m)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if m > n: return 0

        dp = [0] * (m + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                dp[j] = dp[j] + (dp[j - 1] if s[i - 1] == t[j - 1] else 0)

        return dp[m]


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDistinct(s="rabbbit", t="rabbit"))  # 3
    print(sol.numDistinct(s="babgbag", t="bag"))  # 5
    print(sol.numDistinct(s="b", t="b"))  # 1
