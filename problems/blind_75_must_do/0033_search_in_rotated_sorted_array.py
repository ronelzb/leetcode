# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] <= nums[right]:  # pivot (min_value) is in the left half
                if nums[middle] < target <= nums[right]:  # target is in range (mid, last]
                    left = middle + 1
                else:
                    right = middle - 1
            else:  # pivot is in the right half
                if nums[left] <= target < nums[middle]:  # target is in range [first, mid)
                    right = middle - 1
                else:
                    left = middle + 1

        return - 1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search(nums=[1], target=0) == -1
    assert sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert sol.search(nums=[2, 4, 5, 6, 7, 0, 1], target=3) == -1
    assert sol.search(nums=[2, 4, 5, 6, 7, 0, 1], target=5) == 2
    assert sol.search(nums=[3, 1], target=0) == -1
