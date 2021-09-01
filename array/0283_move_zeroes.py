# https://leetcode.com/problems/move-zeroes/
# tags: #array, #two_pointers
#
# Shift zero values to the end of the array
#
# Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        right = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] == 0 and right > i:
                nums.insert(right, nums.pop(i))
                right -= 1
                i -= 1

        print(nums)


if __name__ == "__main__":
    sol = Solution()

    sol.moveZeroes(nums=[0, 1, 0, 3, 12])  # [1, 3, 12, 0, 0]
    sol.moveZeroes(nums=[0])  # [0]
