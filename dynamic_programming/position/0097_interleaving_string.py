# https://leetcode.com/problems/interleaving-string/
# tags: #dp, #string
#
# Solution: Dynamic Programming
# DP table represents if s3 is interleaving at (i+j)th position when s1 is at ith position, and s2 is at jth position.
# 0th position means empty string.
#
# So if both s1 and s2 is currently empty, s3 is empty too, and it is considered interleaving.
# If only s1 is empty, then if previous s2 position is interleaving and current s2 position char is equal to s3
# current position char, it is considered interleaving.
# Similar idea applies to when s2 is empty. when both s1 and s2 is not empty, then if we arrive i, j from i-1, j,
# then if i-1,j is already interleaving and i and current s3 position equal, it s interleaving.
# If we arrive i,j from i, j-1, then if i, j-1 is already interleaving and j and current s3 position equal.
# It is interleaving.
# Time complexity: O(m*n), Space complexity O(n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if l != m + n: return False
        dp = [True] * (n + 1)

        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s3[j - 1] == s2[j - 1]

        for i in range(1, m + 1):
            dp[0] = dp[0] and s3[i - 1] == s1[i - 1]
            for j in range(1, n + 1):
                dp[j] = (dp[j - 1] and s3[i + j - 1] == s2[j - 1]) or (dp[j] and s3[i + j - 1] == s1[i - 1])

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))  # True
    print(sol.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))  # False
    print(sol.isInterleave(s1="", s2="", s3=""))  # True
