# https://leetcode.com/problems/koko-eating-bananas/
# tags: #array, #binary_search
#
# Solution: Binary Search
# Non-trivial binary search problem
# We need to determine whether Koko can finish all bananas within H hours with hourly eating speed
# The lower bound of the search space is 1, and upper bound is max(piles).
# time will be the sum of all elements of piles divided by the current evaluated middle
# We are basically looking for if time <= H based on each pile segmentation of the current K (middle)
# Also, as the problem states "minimum" we are searching the upper bound (left, right], until we reach the optimal value
# Time complexity: O(n*log(n)) n=len(piles), Space complexity O(1)
from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            middle = (left + right) // 2
            time = sum((pile - 1) // middle + 1 for pile in piles)

            if time > h:
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed(piles=[3, 6, 7, 11], h=8))  # 4
    print(sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))  # 30
    print(sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))  # 23
