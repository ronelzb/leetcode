# https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_subproblem(start: int, end: int) -> int:
            current, prev = 0, 0

            for i in range(start, end):
                current, prev = max(current, prev + nums[i]), current

            return max(current, prev)

        return max(rob_subproblem(0, n - 1), rob_subproblem(1, n))


if __name__ == "__main__":
    sol = Solution()
    assert sol.rob(nums=[2, 3, 2]) == 3
    assert sol.rob(nums=[1, 2, 3, 1]) == 4
