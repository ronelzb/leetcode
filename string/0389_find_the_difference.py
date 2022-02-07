# https://leetcode.com/problems/find-the-difference/
# tags:
#
# Solution 1: Counter
# Use a counter for each string and the difference will calculate the result
# Time complexity: O(m+n), Space complexity O(m+n)
#
# Solution 2: Difference
# As we only have 1 additional letter in t we can infer:
# letter_code = sum(letters in t) - sum(letters in s)
# Eventually, we need to convert the letter code back to string
# Time complexity: O(m+n), Space complexity O(1)
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [key for key in (Counter(t) - Counter(s)).keys()][0]

    def findTheDifference_sum(self, s: str, t: str) -> str:
        return chr(sum([ord(c) for c in t]) - sum([ord(c) for c in s]))


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference_sum(s="a", t="aa"))  # "a"
    print(sol.findTheDifference_sum(s="abcd", t="abcde"))  # "e"
