# https://leetcode.com/problems/first-missing-positive/
# tags: #array, #hash_table
#
# Intuitive thinking to the solution:
# https://leetcode.com/problems/first-missing-positive/discuss/319270/Explanation-of-crucial-observation-needed-to-deduce-algorithm
#
# Solution: Swapping misplaced numbers
# Consider position with A[i] = i+1 as a CORRECT SLOT.
# CORRECT SLOT will never be changed: for CORRECT SLOT, A[A[i] - 1] always equals to A[i], vice versa (1)
# For each swap, the number of CORRECT SLOT increases by at least 1: Position A[A[i] - 1] = A[i]
# becomes a CORRECT SLOT after swap, and according to (1), this must be a new CORRECT SLOT
# The maximum of CORRECT SLOT <= N
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        for i in range(n):
            if nums[i] != i + 1: return i + 1

        return n + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive(nums=[3, 4, -1, 1]))  # 1
    print(sol.firstMissingPositive(nums=[7, 8, 9, 11, 12]))  # 1
