# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# tags: #array, #hash_table
#
# Solution: Two pass
# Completeness: change nums[n-1] to -1 for all n in nums, meaning that we have seen n in nums.
# Then we traverse nums once more, and record all indices idx such that nums[idx] != -1.
# Each idx+1 will be a number that disappears in nums
# Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            while n > 0:
                temp = nums[n - 1]
                nums[n - 1] = -1
                n = temp

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    sol = Solution()
    assert sol.findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert sol.findDisappearedNumbers(nums=[1, 1]) == [2]
