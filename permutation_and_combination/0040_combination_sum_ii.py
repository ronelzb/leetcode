# https://leetcode.com/problems/combination-sum-ii/
# tags: #array, #backtracking, #dfs
#
# Solution 1: DFS into Backtracking
# Classical backtracking solution as we need to find all possible unique number combinations equals to target.
# We need to take special consideration that the numbers can be repeated in the input array.
# Because of this, we sort the array at the beginning and at each level we check if the current value equals previous.
# Time Complexity: O(n*log(n) + 2^n) => O(2^n) since we can either include or skip a number
# Space complexity: O(n)
#
# Solution 2: Dynamic Programming
# Variant of knapsack problem
# For each num in candidates(sorted), dp[t] stores all possible combinations forming that num,
# without duplicates up until that num.
# for each candidate in candidates, pick the current num and check if the remaining sum(target-num)
# can be formed by looking in previous table.
# Time Complexity: O(n^2), Space Complexity
from typing import List


class Solution:
    def combinationSum2_dfs(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(start: int, weave: List[int], current_sum: int) -> None:
            if start == n or current_sum >= target:
                if current_sum == target:
                    combinations.append(tuple(weave))
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]: continue
                candidate = candidates[i]
                backtracking(i + 1, weave + [candidate], current_sum + candidate)

        candidates.sort()
        n = len(candidates)
        combinations = []
        backtracking(0, [], 0)
        return combinations

    def combinationSum2_dp(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [{()}] + [set() for _ in range(target)]

        for candidate in sorted(candidates):
            for i in range(target, candidate - 1, -1):
                dp[i] |= {sublist + (candidate,) for sublist in dp[i - candidate]}

        return list(map(list, dp[target]))


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2_dp(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))  # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(sol.combinationSum2_dp(candidates=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                 target=27))
