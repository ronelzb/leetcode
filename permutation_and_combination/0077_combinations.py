# https://leetcode.com/problems/combinations/
# tags: #backtracking, #dfs, #microsoft
#
# Solution: Backtracking
# Classic backtracking problem to iterate from 1 to n - (k - m), to get distinct combinations without
# the need of extra validations
# Time Complexity: O(n*k!), Space complexity: O(n*k)
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(x: int, weave: List[int]) -> None:
            m = len(weave)
            if m == k:
                combinations.append(weave)
                return

            for i in range(x, n - (k - 1 - m)):
                backtracking(i + 1, weave + [i + 1])

        combinations = []
        backtracking(0, [])
        return combinations


if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(n=4, k=2))  # [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
