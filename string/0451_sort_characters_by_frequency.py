# https://leetcode.com/problems/sort-characters-by-frequency/
# tags: #hash_table, #string
#
# Solution: Using Counter to store each character and its frequency
# Time Complexity: O(n*log(m)), Space complexity: O(n)
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([c * count for c, count in Counter(s).most_common()])


if __name__ == "__main__":
    sol = Solution()
    print(sol.frequencySort(s="tree"))  # "eert"
    print(sol.frequencySort(s="Aabb"))  # "bbAa"
