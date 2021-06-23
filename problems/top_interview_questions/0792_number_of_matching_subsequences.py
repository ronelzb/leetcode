# https://leetcode.com/problems/number-of-matching-subsequences/
from bisect import bisect
from collections import defaultdict
from typing import List


class Solution:
    END_OF_WORD = "*"

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexes = defaultdict(list)
        words_found = 0

        for w in words:
            indexes[w[0]].append((1, w))

        for c in s:
            if c in indexes:
                next_index = indexes[c]
                del indexes[c]

                for i, w in next_index:
                    if i == len(w):
                        words_found += 1
                    else:
                        indexes[w[i]].append((i + 1, w))

        return words_found


if __name__ == "__main__":
    sol = Solution()

    assert sol.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]) == 3
