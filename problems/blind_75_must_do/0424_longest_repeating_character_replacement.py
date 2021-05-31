# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import Counter


class Solution:

    # Solution: https://aaronice.gitbook.io/lintcode/two_pointers/longest-repeating-character-replacement
    # Use a variation of sliding window: end - start + 1 - max_count until end - start + 1 - max_count <= k
    def characterReplacement(self, s: str, k: int) -> int:
        start, max_count, max_length = 0, 0, 0
        counter = Counter()

        for end in range(len(s)):
            counter[s[end]] += 1
            max_count = max(max_count, counter[s[end]])

            if end - start + 1 - max_count > k:
                counter[s[start]] -= 1
                start += 1

        return end - start + 1


if __name__ == "__main__":
    sol = Solution()

    assert sol.characterReplacement(s="ABAB", k=2) == 4
