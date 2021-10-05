# https://leetcode.com/problems/jump-game-ii/
# tags: #array, #dp, #greedy
#
# Solution 1: Greedy, BFS variant
# Let's say the range of the current jump is [start, current], farthest is the farthest point that all points
# in [start, current] can reach.
# Once the i reaches current, then trigger another jump, and set the new current with farthest
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps, current, farthest = 0, 0, 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current:
                jumps += 1
                current = farthest

        return jumps


if __name__ == "__main__":
    sol = Solution()
    print(sol.jump(nums=[2, 3, 0, 1, 4]))  # 2
    print(sol.jump(nums=[1, 1, 1, 1]))  # 3
    print(sol.jump(nums=[7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]))  # 2
