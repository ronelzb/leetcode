# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# tags: #hash_table, #sliding_window, #string
#
# Solution: Sliding Window
# Classical sliding window solution. The idea here is to initially count p letters and the first len(p) - 1 letters in s
# Then traverse s from len(p) - 1 to the end trying to find a match to the initial counter_p
# To simplify code using Python built-in Counter comparison we need to delete those letters which are depleted.
# Time complexity: O(m) m=len(s), Space complexity O(n) n=len(p)
from collections import Counter

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = []
        m, n = len(s), len(p)
        if n > m: return []

        counter_p = Counter(p)
        counter_s = Counter(s[:n - 1])

        for i in range(n - 1, m):
            c = s[i]
            counter_s[c] += 1

            start = i - (n - 1)
            if counter_s == counter_p:
                anagrams.append(start)
            counter_s[s[start]] -= 1
            if counter_s[s[start]] == 0: del counter_s[s[start]]

        return anagrams


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams(s="cbaebabacd", p="abc"))  # [0,6]
    print(sol.findAnagrams(s="abab", p="ab"))  # [0,1,2]
    print(sol.findAnagrams(s="abaacbabc", p="abc"))  # [3,4,6]
