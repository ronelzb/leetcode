# https://leetcode.com/problems/buildings-with-an-ocean-view/
# tags: #array, #facebook, #monotonic_stack, #stack
#
# Solution 1: Linear Iteration
# For each building, we will compare if the current building's height "covers" previous ones
# Time complexity: O(n), Space complexity: O(n)
#
# # Solution 2: Monotonic Stack
# In this solution we will build a monotonically decreasing stack: We will traverse the array
# from right to left keeping a variable max_height which will keep the tallest buildings
# seen so far, when a taller building is found then we will store it in the stack
# # Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = []
        for i in range(len(heights)):
            while buildings and heights[buildings[-1]] <= heights[i]:
                buildings.pop()
            buildings.append(i)
        return buildings

    def findBuildings_monStack(self, heights: List[int]) -> List[int]:
        buildings = []
        max_height = -1

        for i in range(len(heights) - 1, -1, -1):
            if max_height < heights[i]:
                max_height = heights[i]
                buildings.append(i)

        buildings.reverse()
        return buildings


if __name__ == '__main__':
    sol = Solution()
    print(sol.findBuildings(heights=[4, 2, 3, 1]))  # [0, 2, 3]
    print(sol.findBuildings(heights=[4, 3, 2, 1]))  # [0,1,2,3]
    print(sol.findBuildings(heights=[1, 3, 2, 4]))  # [3]
