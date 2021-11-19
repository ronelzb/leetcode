# https://leetcode.com/problems/gas-station/
# tags: #greedy
#
# Solution: One pass
# The main idea is that every time we go to the next station as far as possible (remained gas is bigger or equal to 0)
# until we can not (remained gas is less than 0).
# Then we must extend our start station to the "last station" (the station before start) to find a possible solution.
# Repeat these two steps until we have checked all stations (start == end).
#
# We can travel around the circuit only if the remained gas is bigger or equal to 0
# Time complexity: O(n), Space complexity O(1)
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, tank, total = 0, 0, 0

        for station in range(len(gas)):
            fuel = gas[station] - cost[station]
            tank += fuel
            total += fuel

            if tank < 0:
                tank = 0
                start = station + 1

        return start if total >= 0 else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))  # 3
    print(sol.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))  # -1
