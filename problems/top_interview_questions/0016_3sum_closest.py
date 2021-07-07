# https://leetcode.com/problems/3sum-closest/
from typing import List


class Solution:
    # We can make a 3 sum problem variant (Good explanation here: https://www.callicoder.com/three-sum-problem/)
    # Sort the initial array, fix and traverse the array and use two pointers to reduce complexity.
    # Compute current sum: nums[i] + nums[left] + nums[right], left and right used as in binary search
    # The important calculation is abs(target - current) < abs(target - closest) to get the approximation each time
    # Time complexity: O(nlog(n) + n^2) => O(n^2)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if abs(target - current) < abs(target - closest):
                    closest = current
                if current < target:
                    left += 1
                else:
                    right -= 1

        return closest


if __name__ == "__main__":
    sol = Solution()

    assert sol.threeSumClosest(nums=[-1, 2, 1, -4], target=1) == 2
