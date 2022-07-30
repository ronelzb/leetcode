# https://leetcode.com/problems/find-and-replace-pattern/
# tags: #array, #hash_map, #string
#
# Solution: Normalise and compare
# Based on @lee215 post:
# https://leetcode.com/problems/find-and-replace-pattern/discuss/161288/C%2B%2BJavaPython-Normalise-Word
# Convert each string to a base pattern and then compare them.
# Time complexity: O(n*c) n=len(words) c=len(word), Space complexity: O(n*c)
from collections import defaultdict
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def normalise(word: str) -> str:
            char_idx = defaultdict(int)
            idx = ord("a")

            for c in word:
                if c not in char_idx:
                    char_idx[c] = idx
                    idx += 1

            return "".join([chr(char_idx[c]) for c in word])

        pattern_matches = []
        pattern_normalised = normalise(pattern)

        for word in words:
            if normalise(word) == pattern_normalised:
                pattern_matches.append(word)

        return pattern_matches


if __name__ == '__main__':
    sol = Solution()
    print(sol.findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))  # ["mee","aqq"]
