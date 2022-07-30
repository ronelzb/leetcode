# https://leetcode.com/problems/word-subsets/
# tags: #array, #hash_table, #string
#
# Solution: Counters
# We need to find elements from words1, for which each string from words2 have less or equal frequencies
# for each symbol. Frequencies variable will have the maximal value for each letter in word2
# Then, calculate the Counter for word1 and check if it is bigger for each element in frequencies
# Time complexity: O(m + n), Space complexity: O(m)
from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        frequencies = Counter()
        for word in words2:
            frequencies |= Counter(word)
            print(frequencies)

        return [word for word in words1 if not frequencies - Counter(word)]


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"],
                          words2=["e", "o"]))  # ["facebook","google","leetcode"]
    print(sol.wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"],
                          words2=["l", "e"]))  # ["apple","google","leetcode"]
