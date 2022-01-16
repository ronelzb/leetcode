# https://leetcode.com/problems/maximize-distance-to-closest-person/
# tags: #array
#
# Solution: One pass
# Loop on all seats, when we met a people, we count the distance from previous occupied seat.
# The final result = max(distance at the beginning, distance in the middle / 2, distance at the end).
# Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        previous_occupied_seat = -1
        max_distance = 0
        n = len(seats)

        for i in range(n):
            if seats[i] == 1:
                if i - previous_occupied_seat > 1:
                    distance = (i - previous_occupied_seat) // 2 if previous_occupied_seat > -1 else i
                    max_distance = max(max_distance, distance)

                previous_occupied_seat = i

        return max(max_distance, n - 1 - previous_occupied_seat)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))  # 2
    print(sol.maxDistToClosest([1, 0, 0, 0]))  # 3
    print(sol.maxDistToClosest([0, 1]))  # 1
