# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# tags: #array, #dp, #top_interview_questions
#
# Solution: Dynamic Programming
# At each price: Find min price after finding max profit
# Time complexity: O(n), Space complexity: O(1)
#
# Variant Solution: Kadane's Algorithm "max subarray problem"
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, sys.maxsize

        for price in prices:
            profit = max(price - min_price, profit)
            min_price = min(price, min_price)

        return profit


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
