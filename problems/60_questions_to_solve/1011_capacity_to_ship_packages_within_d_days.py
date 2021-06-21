# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
from typing import List


class Solution:
    # Idea: https://www.geeksforgeeks.org/capacity-to-ship-packages-within-d-days/
    # This problem can be solved using Greedy and Binary Search techniques.
    # Using max_elem as the maximum element in the array and total_sum as total sum of the array
    # They will be the lower and upper bounds of the search
    # Check if it is possible to ship all the packages within D days when the maximum capacity allowed is middle
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)  # left bound
        right = sum(weights)  # right bound

        while left < right:
            middle, current, store = (left + right) // 2, 0, 1

            for w in weights:
                if current + w > middle:
                    store += 1
                    current = 0
                current += w

            if store > days:
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    sol = Solution()

    assert sol.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5) == 15
