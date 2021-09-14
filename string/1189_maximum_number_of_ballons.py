# https://leetcode.com/problems/maximum-number-of-balloons/
# tags: #counting, #hash_table, #string
#
# Solution: Count of chars
# Time Complexity: O(n), Space complexity: O(26) => O(1)
import sys
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        max_words = sys.maxsize

        for c in "balon":
            if c not in counter:
                return 0
            max_words = min(max_words, counter[c] // (2 if c == "l" or c == "o" else 1))
        return max_words


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNumberOfBalloons(text="loonbalxballpoon"))  # 2
    print(sol.maxNumberOfBalloons(text="balon"))  # 0
