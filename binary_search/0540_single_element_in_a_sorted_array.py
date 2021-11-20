# https://leetcode.com/problems/single-element-in-a-sorted-array/
# tags: #array, #binary_search, #google
#
# Solution: Binary Search on even indexes only
# The basic idea here is that there's only one element that appears once.
# Suppose a series of number that all the elements appear twice, then each number always change at even positions.
# If one number only appears once, then the rule will be broken and we can use binary search based on this rule.
#
# if mid is even, then nums[mid] = nums[mid + 1], single number is >= mid + 2
# if mid is odd, then nums[mid] = nums[mid - 1], single number is >= mid + 1
# Time complexity: O(log(n)), Space complexity O(1)
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            middle = (start + end) // 2
            temp = middle + 1 if middle % 2 == 0 else middle - 1

            if nums[middle] == nums[temp]:
                start = middle + 1
            else:
                end = middle

        return nums[start]


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]))  # 2
    print(sol.singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]))  # 10
    print(sol.singleNonDuplicate(nums=[1, 1, 2, 3, 3]))  # 2
