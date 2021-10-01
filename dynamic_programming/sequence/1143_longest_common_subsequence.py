# https://leetcode.com/problems/longest-common-subsequence/
#
# Solution: Dynamic Programming
# Bottom-up DP utilizes a matrix m where we track LCS sizes for each combination of i and j.
# * If a[i] == b[j], LCS for i and j would be 1 plus LCS till the i-1 and j-1 indexes.
# * Otherwise, we will take the largest LCS if we skip a character from one of the string
# (max(m[i - 1][j], m[i][j - 1]).
# Time complexity: O(m*n), Space complexity: O(m*n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # go backwards and reconstruct lcs
        # for row in dp:
        #     print(row)
        # longest_subsequence = []
        # while dp[m][n] > 0:
        #     print(m, n)
        #     current, up, left, diagonal = dp[m][n], dp[m - 1][n], dp[m][n - 1], dp[m - 1][n - 1]
        #
        #     if current == up + 1 and current == left + 1 and current == diagonal + 1:
        #         longest_subsequence.insert(0, text1[m - 1])
        #         m -= 1
        #         n -= 1
        #     elif current == up or (current == up + 1 and current == left + 1):
        #         m -= 1
        #     else:
        #         n -= 1
        #
        # return "".join(longest_subsequence)

        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()

    assert sol.longestCommonSubsequence(text1="abcde", text2="ace") == 3
