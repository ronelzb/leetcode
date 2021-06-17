# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:

    # Idea: You can think the pairwise difference is recording daily gains instead of sell and buy stock every day.
    # Incremental profit = (prices[i+1] - prices[i]) + (prices[i+2] - prices[i+1]) = prices[i+2] - prices[i]
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(prices[i] - prices[i - 1], 0)

        return profit


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 7
