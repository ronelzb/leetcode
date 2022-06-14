# https://leetcode.com/problems/delete-operation-for-two-strings/
# tags: #dp, #string
#
# Solution: Dynamic Programming - Longest Common Subsequence
# LCS variation solution
# For example: Input strings: s1="sea", s2="eat", LCS="ea"
# Thus, required number of deletions = len(s1) + len(s2) - 2 * len(LCS)
# Time complexity: O(m*n), Space complexity: O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return m + n - 2 * dp[m][n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance(word1="sea", word2="eat"))  # 2
    print(sol.minDistance(word1="leetcode", word2="etco"))  # 4
    print(sol.minDistance(word1="food", word2="money"))  # 7
