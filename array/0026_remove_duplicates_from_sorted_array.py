# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# tags: #array, #two_pointers, #top_interview_questions
#
# Solution: Two pointers
# Have a slow and fast pointers, when nums[slow] != nums[fast] then we change slow + 1 (next number) in-place
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[k]:
                nums[k + 1] = nums[i]
                k += 1

        return k + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates(nums=[1, 1, 2]))  # 2
    print(sol.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # 5
