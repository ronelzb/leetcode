# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return left


if __name__ == "__main__":
    sol = Solution()

    assert sol.searchInsert(nums=[1, 3, 5, 6], target=5) == 2
    assert sol.searchInsert(nums=[1, 3, 5, 6], target=2) == 1
    assert sol.searchInsert(nums=[1, 3, 5, 6], target=7) == 4
    assert sol.searchInsert(nums=[1, 3, 5, 6], target=0) == 0
