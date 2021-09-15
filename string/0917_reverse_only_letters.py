# https://leetcode.com/problems/reverse-only-letters/
# tags: #string, #two_pointers
#
# Solution 1: Two pointer, one pass
# Start at the beginning and the end of the string.
# Find two letters and swap them.
# Time Complexity: O(n), Space complexity: O(1)
#
# Solution 2: Use while clause inside while loop
# Time complexity: O(n), Space complexity: O(1)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        start, end, s = 0, len(s) - 1, list(s)

        while start < end:
            if s[start].isalpha() and s[end].isalpha():
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif not s[start].isalpha():
                start += 1
            else:
                end -= 1

        return "".join(s)

    def reverseOnlyLetters_whileLoop(self, s: str) -> str:
        start, end, s = 0, len(s) - 1, list(s)
        while start < end:
            while not s[start].isalpha(): start += 1
            while not s[end].isalpha(): end -= 1
            if start >= end: break

            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return "".join(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseOnlyLetters_whileLoop(s="ab-cd"))  # "dc-ba"
    print(sol.reverseOnlyLetters_whileLoop(s="a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
    print(sol.reverseOnlyLetters_whileLoop(s="Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"
