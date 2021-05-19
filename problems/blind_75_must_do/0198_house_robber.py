# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_amount = [0] * n
        max_amount[0] = nums[0]
        max_amount[1] = max(nums[0], nums[1])

        for i in range(2, n):
            max_amount[i] = max(max_amount[i - 1], max_amount[i - 2] + nums[i])

        return max_amount[-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.rob(nums=[1, 2, 3, 1]) == 4
