# https://leetcode.com/problems/running-sum-of-1d-array/
# tags: #array, #prefix_sum
#
# Solution: Python built-in method
# There are essentially 2 solutions for this problem:
# 1. Use a Python built-in method
# 2. Traverse the array adding the previous number with the actual and storing the new number in the current index
# Time complexity: O(n), Space complexity: O(n)
from itertools import accumulate
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))


if __name__ == '__main__':
    sol = Solution()
    print(sol.runningSum(nums=[1, 2, 3, 4]))  # [1,3,6,10]
    print(sol.runningSum(nums=[3, 1, 2, 10, 1]))  # [3,4,6,16,17]
