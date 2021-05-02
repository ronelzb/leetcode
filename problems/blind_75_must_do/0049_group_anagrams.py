# https://leetcode.com/problems/group-anagrams/
from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)  # Counter(word): position in the list

        for word in strings:
            c = tuple(sorted(Counter(word).items()))
            anagram_groups[c].append(word)

        return anagram_groups.values()

    def groupAnagramsUsingArray(self, strings: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strings:
            char_frequencies = [0] * 26
            for c in word:
                char_frequencies[ord(c) - 97] += 1

            anagram_groups[tuple(char_frequencies)].append(word)

        return anagram_groups.values()


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagramsUsingArray(strings=["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(sol.groupAnagrams(strings=[""]))
    # print(sol.groupAnagrams(strings=["a"]))
    # print(sol.groupAnagrams(strings=["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]))
