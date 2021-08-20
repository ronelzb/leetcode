# https://leetcode.com/problems/minimum-window-subsequence/
# tags: #dp, #google, #matrix, #sequence, #string
# This problem can be solved as follows:
# We can build a dp matrix in which the subsequence will start at index k of S
# The first step is to find the letter of T found at indices of S, this will be our possible k
# Then, if S[i] == T[i] it means the last character is the same to previous one dp[i][j] = dp[i - 1][j - 1]
# Eventually, we need to reconstruct the minimum subsequence finding each subsequence found in S (dp[i][t - 1] > 1)
# We return an empty string in case we do not find one, where start = -1 after traversing s in the dp
# Time complexity: O(s + s*t + s) => O(st), Space complexity: O(s*t)
import sys


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        s, t = len(S), len(T)
        dp = [[-1] * t for _ in range(s)]

        for i in range(s):
            if S[i] == T[0]:
                dp[i][0] = i
            elif i > 0:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, s):
            for j in range(1, t):
                if S[i] == T[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        start, length = -1, sys.maxsize
        for i in range(s):
            current_start = dp[i][t - 1]
            if current_start > -1:
                new_length = i - current_start + 1
                if new_length < length:
                    length = new_length
                    start = current_start

        return S[start:length + 1] if start > -1 else ""


if __name__ == "__main__":
    sol = Solution()

    print(sol.minWindow(S="abcdebdde", T="bde"))  # bcde
