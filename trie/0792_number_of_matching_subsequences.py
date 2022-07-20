# https://leetcode.com/problems/number-of-matching-subsequences/
# tags: #google, #hash_table, #string, #top_interview_questions, #trie
#
# Solution: Next letter pointer
# We can put words into buckets by starting character
# Then, while iterating through letters of s, we will move our words through different groups
# Every time we find a word in the iteration, the first letter is removed from dictionary since is no longer needed
# Time complexity: O(s+sum(len(w) for w in words)), Space complexity: O(w)
from collections import defaultdict
from typing import List


class Solution:

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_indexes = defaultdict(list)
        words_found = 0

        for w in words:
            word_indexes[w[0]].append((1, w))

        for c in s:
            if c in word_indexes:
                word_index = word_indexes[c]
                del word_indexes[c]

                for ni, w in word_index:
                    if ni == len(w):
                        words_found += 1
                    else:
                        word_indexes[w[ni]].append((ni + 1, w))

        return words_found


if __name__ == "__main__":
    sol = Solution()

    assert sol.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]) == 3
