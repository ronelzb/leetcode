# https://leetcode.com/problems/minimum-window-substring/
# tags: #hash_table, #google, #sliding_window, #string, #two_pointers
# To check if a window is valid, we use a map to store (char, count) for chars in t.
# And use counter for the number of chars of t to be found in s.
#
# The key part is t_counter[s[end]]-= 1, we decrease count for each char in s found in the counter
# At each char in s we decrease the counter, if t_counter[s[end]] > 0 we can update the total chars found
# When the this total chars found exceeds the length of t then we slide the window to
# a new start index where a char is available again.
#
# Time complexity: O(3 * m + n) => O(m + n), Space complexity: O(n)
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        n = len(t)

        start, min_start, min_length = 0, 0, float("inf")
        for i, c in enumerate(s):
            if c in t_counter:
                if t_counter[c] > 0:
                    n -= 1
                t_counter[c] -= 1

            while n == 0:
                if i - start < min_length:
                    min_length = i - start
                    min_start = start

                if s[start] in t_counter:
                    t_counter[s[start]] += 1
                    if t_counter[s[start]] > 0:
                        n += 1

                start += 1

        return s[min_start: min_start + min_length + 1] if min_length < float("inf") else ""


if __name__ == "__main__":
    sol = Solution()

    print(sol.minWindow(s="ADOBECODEBANC", t="ABC"))  # "BANC"
