# https://leetcode.com/problems/break-a-palindrome/
# tags: #greedy, #string
#
# Solution: Greedy
# Traverse half of the palindrome string to find a letter different than "a", swap to "a" and return the result
# If the palindrome if made of only a's then swap the last letter to "b"
# Time Complexity: O(n), Space complexity: O(n)
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n < 2:
            return ""

        s = list(palindrome)
        for i in range(n // 2):
            if s[i] != "a":
                s[i] = "a"
                return "".join(s)

        s[-1] = "b"
        return "".join(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.breakPalindrome(palindrome="abccba"))  # "aaccba"
    print(sol.breakPalindrome(palindrome="aba"))  # "abb"
