# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/
# tags: #bit_manipulation, #google, #hash_table, #sorting, #string
#
# Solution: Sets
# Generate the startWords set
# Look up the targetWords in the startWords set
# Time complexity: O(m+n), Space complexity: O(m+n)
from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def create_word_tuple(s: str):
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord("a")] = 1
            return tuple(chars)

        words = set()
        for word in startWords:
            words.add(create_word_tuple(word))

        res = 0
        for word in targetWords:
            for i in range(len(word)):
                substring = word[:i] + word[i + 1:]

                if create_word_tuple(substring) in words:
                    res += 1
                    break

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordCount(startWords=["ant", "act", "tack"], targetWords=["tack", "act", "acti"]))  # 2
    print(sol.wordCount(startWords=["ab", "a"], targetWords=["abc", "abcd"]))  # 1
