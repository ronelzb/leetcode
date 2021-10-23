# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# tags: #array, #binary_search
#
# Explanation at:
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/167981/Beats-100-Binary-Search-with-Explanations
#
# Solution: Binary Search
# nums[lo] <= nums[mi] > nums[hi], (mi, hi] is not sorted, min is inside
# nums[lo] > nums[mi] <= nums[hi], (lo, mi] is not sorted, min is inside
# nums[lo] <= nums[mi] <= nums[hi], min is nums[lo]
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[left]:
                right = middle
                left += 1
            else:
                right -= 1

        return nums[left]


if __name__ == "__main__":
    sol = Solution()
    # print(sol.findMin(nums=[2, 2, 2, 0, 1]))  # 0
    print(sol.findMin(nums=[3, 3, 1, 3]))  # 1
