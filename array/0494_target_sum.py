# https://leetcode.com/problems/target-sum/
# tags: #backtracking, #dp
#
# Non-optimized Solution: Backtracking
# For reference purposes
# Time complexity: O(2^n), Space complexity O(n^2)
#
# Solution: Dynamic programming
# Based on the brute force solution, once we introduce memoization, we will only solve each sub-problem once.
# Memoization is done per (current, pos) tuple.
# Time complexity: O(n^2), Space complexity O(n^2)
from typing import List


class Solution:
    def __init__(self):
        self.memo = None
        self.expressions = None

    def findTargetSumWays_backtracking(self, nums: List[int], target: int) -> int:
        def backtracking(current: int, pos: int) -> None:
            if pos == n:
                if current == target: self.expressions += 1
                return

            backtracking(current + nums[pos], pos + 1)
            backtracking(current - nums[pos], pos + 1)

        self.expressions = 0
        n = len(nums)
        backtracking(0, 0)
        return self.expressions
    
    def findTargetSumWays_dp(self, nums: List[int], target: int) -> int:
        def backtracking(current: int, pos: int) -> int:
            if (current, pos) in self.memo:
                return self.memo[(current, pos)]
            
            if pos == n:
                return 1 if current == target else 0
            
            positive = backtracking(current + nums[pos], pos + 1)
            negative = backtracking(current - nums[pos], pos + 1)
            self.memo[(current, pos)] = positive + negative
            return self.memo[(current, pos)]
        
        self.memo = dict()
        n = len(nums)
        return backtracking(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTargetSumWays_dp(nums=[1, 1, 1, 1, 1], target=3))  # 5
    print(sol.findTargetSumWays_dp(nums=[1], target=1))  # 1
