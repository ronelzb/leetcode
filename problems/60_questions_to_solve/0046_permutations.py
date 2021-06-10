# https://leetcode.com/problems/permutations/
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
