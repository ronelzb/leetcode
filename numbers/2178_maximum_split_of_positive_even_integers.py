# https://leetcode.com/problems/maximum-split-of-positive-even-integers/
# tags: #google, #greedy, #math
#
# Solution: Two Pointers + Greedy
# Variant problem: [881. Boats to Save People](https://leetcode.com/problems/maximum-split-of-positive-even-integers)
# Starting from the smallest positive even integer, 2, each iteration will subtract finalSum and
# increase our next number to add by 2, until we reach the target or go beyond the final sum
# Time complexity: O(sqrt(n)), Space complexity: O(1)
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []

        even_integers = []
        start = 2

        while start <= finalSum:
            even_integers.append(start)
            finalSum -= start
            start += 2
        even_integers[-1] += finalSum

        return even_integers


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumEvenSplit(finalSum=12))  # [2,4,6]
    print(sol.maximumEvenSplit(finalSum=7))  # []
    print(sol.maximumEvenSplit(finalSum=28))  # [6,8,2,12]
