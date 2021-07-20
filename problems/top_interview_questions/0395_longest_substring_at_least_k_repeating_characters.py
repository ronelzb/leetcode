# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
from collections import defaultdict, Counter


class Solution:
    # Idea: Divide and conquer using the least common char as a separator at each recursion
    # If we find a substring which the least common is equal or greater than k then we return its length
    # Time complexity: O(n) < T(n) < O(n^2), worst case scenario O(n^2), Space complexity O(n^2)
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        least_common_char, count = Counter(s).most_common()[-1]
        if count >= k:
            return n
        return max(self.longestSubstring(c, k) for c in s.split(least_common_char))


if __name__ == "__main__":
    sol = Solution()

    assert sol.longestSubstring(s="ababbc", k=2) == 5
