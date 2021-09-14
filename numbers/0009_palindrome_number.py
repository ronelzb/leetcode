# https://leetcode.com/problems/palindrome-number/
# tags: #math
#
# Solution 1: Compare reversed string
# Convert the number to string and compare it with the reversed string
# Time Complexity: O(n) n=number of digits in number, Space complexity: O(n)
#
# Solution 2: Compare reversed number
# Recreate a new number in reverse order
# Time Complexity: O(n) n=number of digits in number, Space complexity: O(1)
#
# Solution 3: Compare half reversed number
# Instead of reversing the whole integer, let's convert half of the integer and then check if it's palindrome
# Eventually, we compare x == revX, if even length, or x == revX//10 if odd length.
# Time Complexity: O(n/2) n=number of digits in number, Space complexity: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome_followup(self, x: int) -> bool:
        if x < 0:
            return False

        rev_x = 0
        aux = x
        while aux > 0:
            rev_x = rev_x * 10 + aux % 10
            aux //= 10

        return x == rev_x

    def isPalindrome_followup_opt(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        result = 0
        while x > result:
            result = result * 10 + x % 10
            x //= 10

        return x == result or x == result // 10


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome_followup_opt(x=121))  # True
