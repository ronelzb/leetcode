# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Great explanation at:
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:  # (middle,right]
                left = middle + 1
            else:  # [left, middle]
                right = middle

        return nums[left]


if __name__ == "__main__":
    sol = Solution()
    assert sol.findMin(nums=[3, 4, 5, 1, 2]) == 1
    assert sol.findMin(nums=[4, 5, 6, 7, 0, 1, 2]) == 0
    assert sol.findMin(nums=[11, 13, 15, 17]) == 11
    assert sol.findMin(nums=[2, 1]) == 1
    assert sol.findMin(nums=[3, 1, 2]) == 1
