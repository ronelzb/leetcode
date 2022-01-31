# https://leetcode.com/problems/richest-customer-wealth/
# tags: #array, #matrix
#
# Solution: Python built-in methods
# Use sum and max methods to get each row sum and then retrieve the max value between rows
# Time complexity: O(m*n), Space complexity O(1)
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))  # 6
    print(sol.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]))  # 10
    print(sol.maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]))  # 17
