# https://leetcode.com/problems/valid-palindrome-ii/
# tags: #greedy, #microsoft, #string, #two_pointers
#
# Solution: Two pointers
# We can use the standard two-pointer approach that starts at the left and right of the string and move inwards.
# Whenever there is a mismatch, we can either exclude the character at the left or the right pointer.
# Then, we can take the remaining substrings and compare them with its reversed to see if either one is
# a valid palindrome
# Time complexity: O(n) The left-right movement inward is O(N), and the mismatch check which happens a maximum
# of one time is also O(N),
# Space complexity O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                delete_left = s[left + 1: right + 1]
                delete_right = s[left: right]
                return delete_left == delete_left[::-1] or delete_right == delete_right[::-1]

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.validPalindrome(s="aba"))  # True
    print(sol.validPalindrome(s="abca"))  # True
    print(sol.validPalindrome(s="abc"))  # False
