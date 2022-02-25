# https://leetcode.com/problems/first-unique-character-in-a-string/
# tags: #counting, #hash_table, #string, #top_interview_questions
#
# Solution: Counter
# Count all the different chars in the string s
# Traverse the string and the first char which has a count of 1 wins
# Time Complexity: O(n), Space complexity: O(26) => O(1)
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1


if __name__ == "__main__":
    sol = Solution()

    print(sol.firstUniqChar(s="leetcode"))  # 0
    print(sol.firstUniqChar(s="loveleetcode"))  # 2
    print(sol.firstUniqChar(s="aabb"))  # -1
