# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    # We can simply use backtracking to solve this problem
    # The only catch is to append to the unique set the current weave at the beginning of each
    # backtracking call
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []

        def backtracking(sub_list: List[int], weave: List[int] = []) -> None:
            sets.append(weave)

            if not sub_list:
                return

            n = len(sub_list)
            for i in range(n):
                num = sub_list[i]

                backtracking(sub_list[i + 1:n], weave + [num])

        backtracking(nums)
        # print(sets)
        return sets


if __name__ == "__main__":
    sol = Solution()

    sol.subsets(nums=[1, 2, 3])
