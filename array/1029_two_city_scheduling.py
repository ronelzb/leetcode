# https://leetcode.com/problems/two-city-scheduling/
# tags: #array, greedy, #sorting
#
# Solution: Greedy + Sorting
# The idea here is to sort the input array in a way that we are able to iterate and find each optimal cost locally
# Intuition is to find differences b/w the cost of two cities and then the minimum diff is to be added to min_cost
# Now, for each cost[i] get which is the least cost between A and B and allocate it accordingly.
# Time complexity: O(n*log(n)), Space complexity O(1)
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        na_cost, nb_cost, min_cost = 0, 0, 0
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)

        for a_cost, b_cost in costs:
            if (na_cost < n // 2 and a_cost <= b_cost) or nb_cost == n // 2:
                min_cost += a_cost
                na_cost += 1
            else:
                min_cost += b_cost
                nb_cost += 1

        return min_cost


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoCitySchedCost(costs=[[10, 20], [30, 200], [400, 50], [30, 20]]))  # 110
    print(sol.twoCitySchedCost(costs=[[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))  # 1859
    print(sol.twoCitySchedCost(
        costs=[[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]))  # 3086
