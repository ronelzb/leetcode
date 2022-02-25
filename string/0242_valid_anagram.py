# https://leetcode.com/problems/valid-anagram/
# tags: #hash_table, #must_do_easy_questions, #sorting, #string, #top_interview_questions
#
# Solution: Counter
# Compare each string letters' counter
# Time complexity: O(m+n), Space complexity: O(m+n)
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram(s="anagram", t="nagaram"))  # True
    print(sol.isAnagram(s="rat", t="car"))  # False
