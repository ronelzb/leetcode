# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
# tags: #array, #facebook, #hash_table, #sorting
#
# Solution 1: Compare sorted arrays
# Time Complexity: O(n*log(n)), Space complexity: O(1)
#
# Solution 2: Count both arrays values
# Time Complexity: O(n), Space complexity: O(n)
#
# Solution 3: Use Counter
# Time Complexity: O(n), Space complexity: O(n)
from collections import Counter, defaultdict
from typing import List


class Solution:
    def are_they_equal_sort(self, array_a: List[int], array_b: List[int]) -> bool:
        return sorted(array_a) == sorted(array_b)

    def are_they_equal_dict(self, array_a: List[int], array_b: List[int]) -> bool:
        indexes_counter = defaultdict(int)
        for i in range(len(array_a)):
            indexes_counter[array_a[i]] += 1
            indexes_counter[array_b[i]] -= 1

        for index in indexes_counter:
            if indexes_counter[index] != 0: return False

        return True

    def are_they_equal_counter(self, array_a: List[int], array_b: List[int]) -> bool:
        return Counter(array_a) == Counter(array_b)


if __name__ == "__main__":
    sol = Solution()
    print(sol.are_they_equal_sort(array_a=[1, 2, 3, 4], array_b=[1, 4, 3, 2]))  # True
