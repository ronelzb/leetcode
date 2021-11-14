# https://leetcode.com/problems/subsets-ii/
# tags: #array, #backtracking
#
# Solution: Backtracking
# Classical backtracking solution, just pay attention that there must not be any duplicated sub set
# To solve this inner problem we can validate if we're finding a duplicate in the level + 1 of the recursion
# using i > start and nums[i] == nums[i - 1]
# Time complexity: O(n!*n), Space complexity O(n!)
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(weave: List[int], start: int) -> None:
            power_set.append(weave)
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]: continue
                backtracking(weave + [nums[i]], i + 1)

        nums.sort()
        n = len(nums)
        power_set = []
        backtracking([], 0)
        return power_set


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup(nums=[1, 2, 2]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
