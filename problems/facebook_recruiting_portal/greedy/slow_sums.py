# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=836241573518034&c=896138004629128&ppid=454615229006519&practice_plan=0
# Similar to LeetCode question "1000. Minimum Cost to Merge Stones":
# https://leetcode.com/problems/minimum-cost-to-merge-stones/
# Made a first unsuccessful attempt using DP, this solution is purely greedy and needs refinement
# Time Complexity: O(n^2*k), Space complexity: O(n^2)
import sys
from typing import List


class Solution:
    def getTotalTime(self, arr: List[int]) -> int:
        n = len(arr)
        arr = sorted(arr, reverse=True)
        current = arr[0] + arr[1]
        penalty = current

        for i in range(2, n):
            current += arr[i]
            penalty += current

        return penalty


if __name__ == "__main__":
    sol = Solution()
    print(sol.getTotalTime(arr=[4, 2, 1, 3]))  # 26
    print(sol.getTotalTime(arr=[2, 3, 9, 8, 4]))  # 88
    # print(sol.getTotalTime(arr=[7, 8, 1, 7, 8, 7]))  # 128
    # print(sol.getTotalTime(arr=[7, 8, 1, 6, 7, 7]))  # 120
    # print(sol.getTotalTime(arr=[100, 100, 99, 2, 1]))  # 1102
