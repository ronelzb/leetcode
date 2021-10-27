# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# tags: #array, #two_pointers
#
# Solution 1: Two pointers
# A variant from the first problem, as each number can be at most twice
# adding to the condition if number[k] > nums[k-1] will suffice
# Time Complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(2, len(nums)):
            if nums[i] > nums[k] or nums[k] > nums[k - 1]:
                nums[k + 1] = nums[i]
                k += 1

        return k + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))  # 5, nums = [1,1,2,2,3,_]
    print(sol.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))  # 7, nums = [0,0,1,1,2,3,3,_,_]
