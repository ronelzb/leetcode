# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(n)

        for i in range(n):
            current_index = nums[i]
            while current_index != -1:
                next_index = nums[current_index]
                nums[current_index] = -1
                current_index = next_index

        for i, num in enumerate(nums):
            if num > -1:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()

    assert sol.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert sol.missingNumber(nums=[1, 0]) == 2
