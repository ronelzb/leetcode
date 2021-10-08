# https://leetcode.com/problems/length-of-last-word/
# tags: #string
#
# Solution 1: One pass
# Start from the tail of s and move backwards to find the first non-space character.
# Then from this character, move backwards and count the number of non-space characters
# until we pass over the head of s or meet a space character.
# Time Complexity: O(n), Space complexity: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_length, i = 0, len(s) - 1

        while i >= 0 and not s[i].isalpha():
            i -= 1

        while i >= 0 and s[i].isalpha():
            i -= 1
            word_length += 1

        return word_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord(s="Hello World"))  # 5
