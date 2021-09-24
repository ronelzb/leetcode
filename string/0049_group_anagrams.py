# https://leetcode.com/problems/group-anagrams/
# tags: #hash_table, #sorting, #string
#
# Solution 1: Categorize by Count, using Counter + sort
# Use an dict to group the strings by their sorted counterparts.
# Use the sorted string as the key and all anagram strings as the value.
# Since the string only contains lower-case alphabets,
# we can sort them using counting sort to improve the time complexity
# Time complexity: O(n*log(n)*m), Space complexity: O(26*m) => O(m)
#
# Solution 2: Categorize by Count, using array
# Use char[26] as bucket to count the frequency instead of Arrays.sort,
# this can reduce the O(n*log(n)) to O(n) when calculating the key.
# Time complexity: O(n*m), Space complexity: O(26*m) => O(m)
from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)  # Counter(word): position in the list

        for word in strings:
            c = tuple(sorted(Counter(word).items()))
            anagram_groups[c].append(word)

        return list(anagram_groups.values())

    def groupAnagramsUsingArray(self, strings: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strings:
            char_frequencies = [0] * 26
            for c in word:
                char_frequencies[ord(c) - 97] += 1

            anagram_groups[tuple(char_frequencies)].append(word)

        return list(anagram_groups.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagramsUsingArray(strings=["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(sol.groupAnagrams(strings=[""]))
    # print(sol.groupAnagrams(strings=["a"]))
    # print(sol.groupAnagrams(strings=["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]))
