# https://leetcode.com/problems/combination-sum/
# tags: #array, #backtracking, #dfs
#
# Combinatory solution using a classic use of backtracking
# We loop through every element, if adding this element will not exceed the target
# If the target is equal to 0, we have find our solution along this path and we add this path to out solution
#
# Time complexity: O(n^k) n=len(array) / k=length of longest possible combination
# Space complexity: O(m^n) m=target / n=len(array)
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(sub_candidates: List[int], weave=None, cum: int = 0) -> None:
            if weave is None:
                weave = []
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

    print(sol.combinationSum(candidates=[2, 3, 6, 7], target=7))  # [[2, 2, 3], [7]]
    print(sol.combinationSum(candidates=[2, 3, 5], target=8))  # [[2,2,2,2],[2,3,3],[3,5]]
