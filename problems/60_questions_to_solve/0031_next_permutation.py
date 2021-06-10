# https://leetcode.com/problems/next-permutation/
# Idea: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
from typing import List


class Solution:

    # Condensed mathematical description:
    # 1. Find largest index i such that array[i − 1] < array[i].
    # (If no such i exists, then this is already the last permutation.)
    # 2. Find largest index j such that j ≥ i and array[j] > array[i − 1].
    # 3. Swap array[j] and array[i − 1].
    # 4. Reverse the suffix starting at array[i].
    # def checkPermutation() -> bool:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Find longest non-increasing suffix
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # Now i is the head index of the suffix. Are we at the last permutation already?
        if i > 0:
            # Find rightmost element greater than the pivot
            j = n - 1
            while nums[j] <= nums[i - 1]:
                j -= 1

            # Now the value array[j] will become the new pivot
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

            # Reverse the suffix
            nums[i:] = nums[n - 1: i - 1: -1]

        else:
            nums.reverse()

        # print(nums)


if __name__ == "__main__":
    sol = Solution()
    sol.nextPermutation(nums=[3, 2, 1])  # [1, 3, 2]
