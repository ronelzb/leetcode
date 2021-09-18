# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# tags: #array, #binary_search, #hash_table, #sorting, #two_pointers
#
# Solution 1: Counters intersection
# In Python we can leverage of Counter data structure and list comprehension technique
# to make a 1-line solution. Just intersect both counters, iterate on the result
# and for each value duplicate key v times or just use elements built-in method
# Time Complexity: O(n + m), Space complexity: O(n + m)
#
# Solution Follow-up 1: Two pointers
# Classic two pointers iteration where i points to nums1 and j points to nums 2
# Because a sorted array is in ascending order, so if nums1[i] > nums[j], we need to increment j, and vice versa.
# Only when nums1[i] == nums[j], we add it to the result array.
# Time Complexity O(max(n, m)), Space complexity: O(n + m)
#
# Solution Follow-up 2: Binary Search
# Use Binary search if k=len(nums1) is small enough, O(k*log(n)) < O(max(n,m)), otherwise use two pointers method
# To deal with duplicate entry, once you find an entry, all the duplicate element is around that that index,
# so you can do linear search scan afterward.
# Time complexity: O(k*log(n) + n), Space complexity: O(k)
#
# Solution Follow-up 3:
# * External sort, if the two arrays are of similar length
# * Partition nums2 and send to memory into chunks, if one array if much greater than the other.
# * Another method is, store the larger array into disk, and for each element in the shorter array,
#   use “Exponential Search” and search in the longer array
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())

    def intersect_twoPointers(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        res = []

        while i < n and j < m:
            a, b = nums1[i], nums2[j]
            if a < b:
                i += 1
            elif a > b:
                j += 1
            else:
                res.append(a)
                i += 1
                j += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))  # [2,2]
    print(sol.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))  # [4,9]

    print(sol.intersect_twoPointers(nums1=[4, 5, 9], nums2=[4, 4, 8, 9, 9]))  # [4,9]
