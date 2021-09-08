# https://leetcode.com/problems/is-subsequence/
# tags: #binary_search, #dp, #string, #two_pointers
#
# Solution 1: Two pointers
# We need to keep two pointers: one for string s and one for string t.
# Then if we found new symbol in string t, which is equal to symbol in s, we move two pointers by one.
# If we did not found, then we move pointer for t only.
# Time Complexity: O(t), Space complexity: O(1)
#
# Solution 2: Binary search for follow-up question
# If we have a lot strings say S1, S2, ... , Sk, where k is a big number we want to find faster method.
# Let us create for each symbol sorted list of indexes for this symbol.
# Pre-process complexity = Time complexity: O(n), Space complexity: O(n)
# Time complexity for Si: O(k*m*log(n)) k=list of indexes / m=longest m_i / log(n)=binary search
import bisect
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n_s, n_t = len(s), len(t)
        if n_s == 0:
            return True
        if n_s > n_t:
            return False

        index_s = -1
        for c in t:
            if c == s[index_s + 1]:
                index_s += 1
                if index_s == n_s - 1:
                    return True

        return False

    def isSubsequence_followup(self, s: str, t: str) -> bool:
        places = defaultdict(list)
        for i, symbol in enumerate(t):
            places[symbol].append(i)

        current_place = 0
        for symbol in s:
            current_idx = bisect.bisect_left(places[symbol], current_place)
            if current_idx >= len(places[symbol]):
                return False
            current_place = places[symbol][current_idx] + 1

        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.isSubsequence(s="abc", t="ahbgdc")
    assert not sol.isSubsequence(s="axc", t="ahbgdc")
