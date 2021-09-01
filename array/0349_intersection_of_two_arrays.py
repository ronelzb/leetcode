# https://leetcode.com/problems/intersection-of-two-arrays/
# tags: #array, #hash_table, #sorting, #two_pointers
#
# Solution 1: Use set intersection
# Time complexity: O(min(n, m)), Space complexity: O(n + m)
#
# Solution 2: Two pointer. Sort both input arrays and traverse them.
# If first array's element is less than we increment i and if it is greater than we increment j.
# When they are equal we insert the element in res.
# Time complexity: O(n*log(n) + m*log(m)), Space complexity: O(min(n, m))
from typing import List


class Solution:
    def intersection_set(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    def intersection_two_pointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        nums1.sort()
        nums2.sort()
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.add(nums1[i])
                i += 1
                j += 1

        return list(res)


if __name__ == "__main__":
    sol = Solution()

    # print(sol.intersection_set(nums1=[1, 2, 2, 1], nums2=[2, 2]))  # [2]
    print(sol.intersection_two_pointer(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))  # [9,4]

