# https://leetcode.com/problems/car-pooling/
# tags: #greedy, #heap, #prefix_sum, #simulation, #sorting
#
# Solution 1: Sorting + Greedy
# Sort the initial array by from and to numbers and then compare if the car has capacity for each trip
# If any trip intersects then sum the numPassengers together and check the capacity
# We keep on adding passengers, until we reach one end point
# Time complexity: O(n*log(n)), Space complexity O(n)
from collections import deque
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pick_ups = sorted([(trip[1], trip[0]) for trip in trips])
        drop_offs = sorted([(trip[2], trip[0]) for trip in trips])
        current_load, start, end = 0, 0, 0

        while start < len(trips):
            if pick_ups[start][0] < drop_offs[end][0]:
                current_load += pick_ups[start][1]
                start += 1
            else:
                current_load -= drop_offs[end][1]
                end += 1

            if current_load > capacity: return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.carPooling(trips=[[3, 3, 7], [2, 1, 5]], capacity=4))  # False
    print(sol.carPooling(trips=[[3, 3, 7], [2, 1, 5]], capacity=5))  # True
    print(sol.carPooling(trips=[[3, 5, 7], [2, 1, 5]], capacity=3))  # True
    print(sol.carPooling(trips=[[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]], capacity=23))  # True
    print(sol.carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11))  # True

