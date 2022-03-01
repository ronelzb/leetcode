# https://leetcode.com/problems/summary-ranges/
# tags: #array, #two_pointers
#
# Solution: Two pointers
# Use a start pointer to know where the range begins and then iterate through the array
# When a number not part of sequence is found store the previous range
# Time complexity: O(n), Space complexity O(1)
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start, n = 0, len(nums)
        ranges = []

        for i in range(1, n):
            if nums[i] - 1 > nums[i - 1]:
                ranges.append(f"{nums[start]}->{nums[i - 1]}" if i - 1 > start else f"{nums[start]}")
                start = i
            if i == n - 1:
                ranges.append(f"{nums[start]}->{nums[i]}" if i > start else f"{nums[start]}")

        return ranges


if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges(nums=[-1]))  # ["-1"]
    print(sol.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))  # ["0->2","4->5","7"]
    print(sol.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))  # ["0","2->4","6","8->9"]
