# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# tags: #array, #binary_indexed_tree, #greedy, #segment_tree, #sorting
#
# Solution: Sorting
# The intuition in this problem is to find the median for the nums array
# Sort the array and find the median which is the middle number if nums has odd length
# and the average of middle elements if nums has even length
# Traverse the array summing the absolute value between num and the median
# Time complexity: O(n*log(n)), Space complexity O(1)
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        half = n // 2
        moves = 0

        if n % 2 == 0:
            median = (nums[half - 1] + nums[half]) // 2
        else:
            median = nums[half]

        for num in nums:
            moves += abs(median - num)

        return moves


if __name__ == '__main__':
    sol = Solution()
    print(sol.minMoves2(nums=[1, 2, 3]))  # 2
    print(sol.minMoves2(nums=[1, 10, 2, 9]))  # 16
