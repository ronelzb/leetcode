# https://leetcode.com/problems/subsets/
# tags: #array, #backtracking, #dfs, #microsoft
#
# Solution: Recursion
# We can simply use backtracking to solve this problem
# The only catch is to append to the unique set the current weave at the beginning of each backtracking call
# Time complexity: O(n * 2^n), Space complexity: O(2^n) due to stack trace recursion
#
# Solution: Iterative
# Time complexity: O(n * 2^n),
# Space complexity: O(2^n): Generate all combinations from [0,0,0] to [1,1,1]. total 2^3= 8 combinations. ie 2^n
from typing import List


class Solution:
    def subsets_recursion(self, nums: List[int]) -> List[List[int]]:
        sets = []

        def backtracking(sub_list: List[int], weave=None) -> None:
            if weave is None: weave = []
            sets.append(weave)

            for i in range(len(sub_list)):
                backtracking(sub_list[i + 1:], weave + [sub_list[i]])

        backtracking(nums)
        return sets

    def subsets_iterative(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [prev + [num] for prev in res]

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.subsets_recursion(nums=[1, 2, 3]))  # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
