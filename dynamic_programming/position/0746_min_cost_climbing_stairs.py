# https://leetcode.com/problems/min-cost-climbing-stairs/
# tags: #array, #dp
#
# Solution 1: Bottom-Up Dynamic Programming (Tabulation)
# At each step we find the min for the current value + min of the previous 2 steps
# We assign the current step to a first variable (a or down_one) and the result of the previous
# calculation to a second (a or down_two)
# Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]

        for i in range(2, len(cost)):
            min_cost = cost[i] + min(a, b)
            a, b = b, min_cost

        return min(a, b)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostClimbingStairs(cost=[10, 15, 20]))  # 15
    print(sol.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
