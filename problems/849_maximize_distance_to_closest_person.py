from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        previous_occupied_seat = -1
        max_distance = -1
        n = len(seats)

        for i in range(n):
            if seats[i] == 1:
                if i - previous_occupied_seat > 1:
                    distance = (i - previous_occupied_seat) // 2 if previous_occupied_seat > -1 else i
                    max_distance = max(max_distance, distance)

                previous_occupied_seat = i

        max_distance = max(max_distance, n - 1 - previous_occupied_seat)

        return max_distance


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
    assert sol.maxDistToClosest([1, 0, 0, 0]) == 3
    assert sol.maxDistToClosest([0, 1]) == 1
