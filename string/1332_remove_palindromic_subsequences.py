# https://leetcode.com/problems/break-a-palindrome/
# tags: #string, #two_pointers
#
# Solution: Two pointers
# Max 2 operations solution:
# * if it's empty return 0
# * if the whole word is palindrome return 1
# * Otherwise, we need to make 2 operations
# Time Complexity: O(n), Space complexity: O(1)
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 0 if not s else 1 if s == s[::-1] else 2


if __name__ == '__main__':
    sol = Solution()
    print(sol.removePalindromeSub("ababa"))  # 1
    print(sol.removePalindromeSub("abb"))  # 2
    print(sol.removePalindromeSub("baabb"))  # 2
