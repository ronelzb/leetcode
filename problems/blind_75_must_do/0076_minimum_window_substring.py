# https://leetcode.com/problems/minimum-window-substring/
# Sliding window variation: https://medium.com/kode-shaft/solve-minimum-window-substring-problem-9cb3544eeb91
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        map_chars = Counter(t)
        counter = len(t)
        min_start, start = 0, 0
        min_length = float("inf")

        for i, c in enumerate(s):
            if c in map_chars:
                if map_chars[c] > 0:
                    counter -= 1
                map_chars[c] -= 1

            while counter == 0:
                if i - start < min_length:
                    min_length = i - start
                    min_start = start

                if s[start] in map_chars:
                    map_chars[s[start]] += 1
                    if map_chars[s[start]] > 0:
                        counter += 1
                start += 1

        return s[min_start: min_start + min_length + 1] if min_length < float("inf") else ""


if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert sol.minWindow(s="a", t="a") == "a"
