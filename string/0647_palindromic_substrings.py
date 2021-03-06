# https://leetcode.com/problems/palindromic-substrings/
# tags: #blind_75_must_do, #dp, #string
#
# Solution 1: odd + even substrings
# For each mid point i, use two points (left, right) to check the values on i's left and right sides respectively
# Time complexity: O(n^2), Space complexity: O(1)
#
# Solution 2: DP based on longest palindromic substring
# Reuse a previously computed palindrome to compute a larger palindrome
# reverse range for i: this is bc dp[i][j] depends on dp[i+1][j-1], we need to check larger i first
# Time complexity: O(n^2), Space complexity: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count_palindromes = 0

        for i in range(n):
            # odd substring
            start, end = i, i
            while start >= 0 and end < n and s[start] == s[end]:
                count_palindromes += 1
                start -= 1
                end += 1

            # even substring
            start, end = i - 1, i
            while start >= 0 and end < n and s[start] == s[end]:
                count_palindromes += 1
                start -= 1
                end += 1

        return count_palindromes

    def countSubstrings_dp(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count_palindromes = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
                if dp[i][j]: count_palindromes += 1

        return count_palindromes


if __name__ == "__main__":
    sol = Solution()

    # assert sol.countSubstrings(s="abc") == 3
    # assert sol.countSubstrings(s="aaa") == 6

    assert sol.countSubstrings_dp(s="dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg") == 77
