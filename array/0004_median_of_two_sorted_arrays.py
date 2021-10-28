# https://leetcode.com/problems/median-of-two-sorted-arrays/
# tags: #array, #binary_search, #divide_and_conquer
#
# Optimal solution (if you dare):
# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
#
# Solution: Find the median by traversing
# Time Complexity: O(m+n), Space complexity: O(1)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        ia, ma, ib, mb = 0, 0, 0, 0

        for i in range((n + m) // 2 + 1):
            ma = mb

            if ia == n:
                mb = nums2[ib]
                ib += 1
            elif ib == m:
                mb = nums1[ia]
                ia += 1
            elif nums1[ia] < nums2[ib]:
                mb = nums1[ia]
                ia += 1
            else:  # nums1[ia] >= nums2[ib]
                mb = nums2[ib]
                ib += 1

        if (n + m) % 2 == 0:
            return (ma + mb) / 2

        return mb


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))  # 2.5
