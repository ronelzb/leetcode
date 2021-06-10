# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(sub_candidates: List[int], weave: List[int] = [], cum: int = 0) -> None:
            if cum >= target:
                if cum == target:
                    combinations.append(weave)
                return

            n = len(sub_candidates)

            for i in range(n):
                candidate = sub_candidates[i]
                j = 1

                while cum + candidate * j <= target:
                    backtracking(sub_candidates[i + 1:n],
                                 weave + [candidate] * j, cum + candidate * j)
                    j += 1

        backtracking(candidates)
        return combinations


if __name__ == "__main__":
    sol = Solution()

    sol.combinationSum(candidates=[2, 3, 6, 7], target=7)  # [[2, 2, 3], [7]]
    sol.combinationSum(candidates=[2, 3, 5], target=8)  # [[2,2,2,2],[2,3,3],[3,5]]
