# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# tags: #hash_table, #sliding_window, #string
#
# Solution: Two-map
# We use a dict counter to record the expected times of each word found in words and another
# seen to record the times we have seen each word in s.
# Then we check for every possible position of i.
# Once we meet an unexpected word or the times of some word is larger than its expected times, we stop the check.
# If we finish the check successfully, push i to the result indexes.
# Time Complexity: O(s*m*n)
# Space complexity: O(m+n): due to dict(words) and substring method(creates a new copy of sub array).
from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_count = Counter(words)
        m, n = len(words), len(words[0])
        res = []

        for i in range(len(s) - m * n + 1):
            seen = defaultdict(int)
            for j in range(i, i + m * n, n):
                lookup_word = s[j: j + n]
                if lookup_word in words_count:
                    seen[lookup_word] += 1
                    if seen[lookup_word] > words_count[lookup_word]:
                        break
                else:
                    break
            if seen == words_count:
                res.append(i)

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))  # [0,9]
