# https://leetcode.com/problems/longest-palindromic-substring/
# tags: #string
#
# Solution: odd + even substrings
# For each mid point i, use two points (left, right) to check the values on i's left and right sides respectively
#
# Time complexity: O(n^2), Space complexity: O(1)
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


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome(s="babad") == "bab" or "aba"
    assert sol.longestPalindrome(s="cbbd") == "bb"
    assert sol.longestPalindrome(s="a") == "a"
    assert sol.longestPalindrome(s="ac") == "a"
    assert sol.longestPalindrome(s="bb") == "bb"
    assert sol.longestPalindrome(s="ccc") == "ccc"
