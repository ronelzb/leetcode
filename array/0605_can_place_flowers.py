# https://leetcode.com/problems/can-place-flowers/
# tags: #array, #greedy
#
# Solution: Greedy
# To avoid coding for the edge cases, consider instead the array [0] + A + [0].
# For each plot from left to right, if we can plant a flower there, then do so.
# We can plant a flower if both neighbors are zeroes.
# Time complexity: O(n), Space complexity O(1)
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        previous_planted, max_flowers = -1, 0
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 1:
                continue
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                max_flowers += 1
                flowerbed[i] = 1
        return max_flowers >= n


if __name__ == "__main__":
    sol = Solution()
    print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2))  # True
    print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))  # True
    print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))  # False
    print(sol.canPlaceFlowers(flowerbed=[1, 0], n=1))  # False
    print(sol.canPlaceFlowers(flowerbed=[0], n=1))  # True
