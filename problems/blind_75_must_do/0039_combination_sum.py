# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(permutation, weave, current_sum) -> None:
            if current_sum >= target:
                if current_sum == target:
                    combinations.append(weave)
                return

            for i in range(len(permutation)):
                next_permutation = permutation[i + 1:]

                j = 1
                while current_sum + permutation[i] * j <= target:
                    new_list = [permutation[i]] * j
                    backtracking(next_permutation,  weave + new_list, current_sum + permutation[i] * j)
                    j += 1

        backtracking(candidates, [], 0)
        return combinations


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum(candidates=[2, 3, 6, 7], target=7))  # [[2,2,3],[7]]
    print(sol.combinationSum(candidates=[2, 3, 5], target=8))  # [[2,2,2,2],[2,3,3],[3,5]]
    print(sol.combinationSum(candidates=[2], target=1))  # []
    print(sol.combinationSum(candidates=[1], target=1))  # [[1]]
    print(sol.combinationSum(candidates=[1], target=2))  # [[1,1]]
