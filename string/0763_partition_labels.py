# https://leetcode.com/problems/partition-labels/
# tags: #greedy, #hash_table, #two_pointers
#
# Solution 1: Dictionary + set
# Keep 2 data structures:
# * Initialize a Counter that will be store the remaining count for each letter
# * A set which will hold all letters that still have count along the way
# We can communicate the Counter with the set saying that when the counter of a letter reaches zero
# then remove it from the set, if the set is empty then we can say it's a valid partition
# Time complexity: O(n), Space complexity O(n)
#
# Solutions 2: Dictionary + two pointers
# Figure out the rightmost index first and use it to denote the start of the next partition.
# A smart way to store the rightmost index for each letter is to traverse the string storing the index
# for each visited letter.
# We can figure that there is a partition when end = max(letters found) == i
# Store the difference of right and left pointers + 1 as in the result for each partition.
# Time complexity: O(n), Space complexity O(n)
from collections import Counter
from typing import List


class Solution:
    def partitionLabels_dict(self, s: str) -> List[int]:
        letters_count = Counter(s)
        letters_found = set()
        partitions = []
        start = 0

        for i, c in enumerate(s):
            letters_count[c] -= 1
            if letters_count[c] > 0:
                letters_found.add(c)
            elif c in letters_found:
                letters_found.remove(c)

            if not letters_found:
                partition_size = i + 1 - start
                partitions.append(partition_size)
                start = i + 1

        return partitions

    def partitionLabels_twoPointers(self, s: str) -> List[int]:
        rightmost_letter = {c: i for i, c in enumerate(s)}
        start, end = 0, 0
        partitions = []

        for i, c in enumerate(s):
            end = max(end, rightmost_letter[c])

            if i == end:
                partitions.append(i + 1 - start)
                start = i + 1

        return partitions


if __name__ == "__main__":
    sol = Solution()
    print(sol.partitionLabels_twoPointers(s="ababcbacadefegdehijhklij"))  # [9,7,8]
    print(sol.partitionLabels_twoPointers(s="eccbbbbdec"))  # [10]
