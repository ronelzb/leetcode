from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        # To avoid coding for the edge cases, consider instead the array [0] + A + [0].
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 1:
                continue

            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1

        return count >= n


if __name__ == "__main__":
    sol = Solution()
    assert sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1)
    assert not sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2)
