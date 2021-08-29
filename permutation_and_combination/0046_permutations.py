# https://leetcode.com/problems/permutations/
# tags: #array, #backtracking, #dfs
#
# Classic backtracking problem.
# Permute n numbers, we can add the nth number into the resulting weave list from the n-1 numbers,
# in every possible position, and dfs cropping last seen number at each drill down.
#
# Time and space complexity explanation:
# https://leetcode.com/problems/permutations/discuss/993970/Python-4-Approaches-%3A-Visuals-%2B-Time-Complexity-Analysis
# Time complexity: O(n * n!), Space complexity(n!)
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtracking(sub_list: List[int], weave: List[int] = []) -> None:
            if not sub_list:
                permutations.append(weave)

            n = len(sub_list)
            for i in range(n):
                num = sub_list[i]

                backtracking(sub_list[:i] + sub_list[i + 1:n], weave + [num])

        backtracking(nums)
        return permutations


if __name__ == "__main__":
    sol = Solution()
    sol.permute(nums=[1, 2, 3])  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
