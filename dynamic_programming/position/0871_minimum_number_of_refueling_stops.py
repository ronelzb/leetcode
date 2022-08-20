# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# tags: #array, #dp, #greedy, #heap
#
# Solution: Max-heap
# We traverse every station getting their position and gas available
# At every station check if we have enough gas to reach the next station
# If the car runs out of fuel (we can't reach the next station)
# * Get the largest gas station available, refuel and add 1 to the total stops
# * If we already visited all previous gas stations available then we cannot drive thus return -1
# Return the number of stops count
# Time complexity: O(n*log(n)), Space complexity: O(n)
import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        stops, prev = 0, 0
        fuel = startFuel
        gas_stations_available = []

        for position, gas in stations:
            distance, prev = position - prev, position

            if fuel < distance:
                while gas_stations_available and fuel < distance:
                    fuel += -heapq.heappop(gas_stations_available)
                    stops += 1

                if fuel < distance:
                    return -1

            fuel -= distance
            heapq.heappush(gas_stations_available, -gas)

        return stops


if __name__ == '__main__':
    sol = Solution()
    print(sol.minRefuelStops(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]]))  # 2
