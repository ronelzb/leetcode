# https://leetcode.com/problems/valid-palindrome/
# tags: #string, #two_pointers
#
# Solution: Two pointers
# Move 2 pointers from each end until they collide.
# * Increment left pointer if not alphanumeric.
# * Decrement right pointer if no alphanumeric.
# * Exit and return error if pointers don't match.
# Time complexity: O(n), Space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            while not s[start].isalnum() and start < end:
                start += 1

            while not s[end].isalnum() and start < end:
                end -= 1

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.isPalindrome(s="A man, a plan, a canal: Panama")
    assert not sol.isPalindrome(s="race a car")
    assert sol.isPalindrome(s=".,")
