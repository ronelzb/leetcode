# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# tags: #array, #dp, #greedy, #top_interview_questions, #top_interview_questions
#
# Solution: Dynamic Programming
# Idea: You can think the pairwise difference is recording daily gains instead of sell and buy stock every day.
# Incremental profit = (prices[i+1] - prices[i]) + (prices[i+2] - prices[i+1]) = prices[i+2] - prices[i]
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/1569093/C%2B%2BPython-Clean-and-Simple-Solution-w-Detailed-Explanation-and-Images-or-Buy-Low-Sell-High
# Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1])


if __name__ == "__main__":
    sol = Solution()

    print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))  # 7
