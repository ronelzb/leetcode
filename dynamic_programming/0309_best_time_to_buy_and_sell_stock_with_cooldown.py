# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# tags: #array, #dp
#
# Solution 1: Dynamic Programming + State machine
# There are 3 states, by the actions one can take. One can calculate the profit at a state at each time:
# s0[i] = max(s0[i - 1], s2[i - 1]); // Stay at s0, or rest from s2
# s1[i] = max(s1[i - 1], s0[i - 1] - prices[i]); // Stay at s1, or buy from s0
# s2[i] = s1[i - 1] + prices[i]; // Only one way from s1
# Time Complexity: O(n), Space complexity: O(1)
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, purchased, rest = 0, -(sys.maxsize - 1), 0
        for price in prices:
            prev = sold
            sold = purchased + price
            purchased = max(purchased, rest - price)
            rest = max(rest, prev)

        return max(sold, rest)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(prices=[1, 2, 3, 0, 2]))  # 3
