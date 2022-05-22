# https://leetcode.com/problems/longest-palindromic-substring/
# tags: #dp, #string
#
# Solution 1: odd + even substrings
# For each mid point i, use two points (left, right) to check the values on i's left and right sides respectively
# Time complexity: O(n^2), Space complexity: O(1)
#
# Solution 2: DP
# Bottom-up apprach: Reuse a previously computed palindrome to compute a larger palindrome
# reverse range for i: this is bc dp[i][j] depends on dp[i+1][j-1], we need to check larger i first
# Time complexity: O(n^2), Space complexity: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        max_start = max_end = 0
        n = len(s)

        for i in range(1, n):
            # check odd substring ending at i
            start, end = i - 1, i + 1
            while start >= 0 and end < n and s[start] == s[end]:
                if end - start + 1 > max_length:
                    max_start = start
                    max_end = end
                    max_length = end - start + 1

                start -= 1
                end += 1

            # check even substring ending at i
            start, end = i - 1, i
            while start >= 0 and end < n and s[start] == s[end]:
                if end - start + 1 > max_length:
                    max_start = start
                    max_end = end
                    max_length = end - start + 1

                start -= 1
                end += 1

        return s[max_start: max_end + 1]

    def longestPalindrome_dp(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = s[0]
        max_length = 1

        for i in range(n):
            dp[i][i] = True

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if max_length < end - start + 1:
                            max_length = end - start + 1
                            res = s[start: end + 1]

        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome_dp(s="babad") == "bab" or "aba"
    assert sol.longestPalindrome(s="cbbd") == "bb"
    assert sol.longestPalindrome(s="a") == "a"
    assert sol.longestPalindrome(s="ac") == "a"
    assert sol.longestPalindrome(s="bb") == "bb"
    assert sol.longestPalindrome(s="ccc") == "ccc"
