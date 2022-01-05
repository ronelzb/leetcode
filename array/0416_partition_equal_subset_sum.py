# https://leetcode.com/problems/partition-equal-subset-sum/
# tags: #array, #dp
#
# Brute-Force solution
# For demo purposes, it can be solved using backtracking
# # Time complexity: O(2^n), Space complexity O(n)
#
# Solution: Dynamic Programming
# Great explanation at:
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/462699/Whiteboard-Editorial.-All-Approaches-explained.
# Solution is similar to Knapsack problem:
# dp[sum] will denote whether sum is achievable or not.
# Initially, we have dp[0] = true since a 0 sum is always achievable.
# Then for each element num, we will iterate & find if it is possible to form a sum j by adding num to
# some previously formable sum.
# Time complexity: O(n*sum), Space complexity O(sum)
from typing import List


class Solution:
    def canPartition_backtracking(self, nums: List[int]) -> bool:
        def backtracking(subset: List[int], current_sum: int) -> bool:
            for i in range(len(subset)):
                new_sum = current_sum + subset[i]
                new_set = subset[:i] + subset[i + 1:]
                if new_sum == sum(new_set) or backtracking(new_set, new_sum): return True

            return False

        return backtracking(nums, 0)

    def canPartition_dp(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0: return False

        half_sum = total_sum // 2
        dp = [True] + [False] * half_sum

        for num in nums:
            for j in range(half_sum, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[half_sum]


if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartition_dp(nums=[1, 5, 11, 5]))  # True
    print(sol.canPartition_dp(nums=[1, 2, 3, 5]))  # False
    print(sol.canPartition_dp(nums=[1, 3, 4, 4]))  # False
