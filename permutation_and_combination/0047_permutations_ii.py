# https://leetcode.com/problems/permutations-ii/
# tags: #array, #backtracking, #dfs
#
# Solution: Backtracking
# Backtracking solution with a twist: As the problem implies we need to find all unique permutations
# To handle duplicates in the input array we can initially sort it and before going down further
# into the backtracking check if the current number we're visiting repeats
# Time Complexity: O(n*log(n) + n*n!) => O(n*n!), Space complexity: O(n!)
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(sub_nums: List[int], weave: List[int]):
            if not sub_nums:
                permutations.append(weave)
                return

            for i in range(len(sub_nums)):
                if i > 0 and sub_nums[i] == sub_nums[i - 1]: continue
                backtracking(sub_nums[:i] + sub_nums[i + 1:], weave + [sub_nums[i]])

        permutations = []
        nums.sort()
        backtracking(nums, [])
        return permutations


if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique(nums=[1, 1, 2]))  # Solution
