# https://leetcode.com/problems/contains-duplicate/
# tags: #array, #hash_table, #sorting, #top_interview_questions
#
# Solution 1: Dictionary
# Compare if the input array length it's the same as its set counterpart
# Time complexity: O(n), Space complexity: O(n)
#
# Solution 1: Sort array + One pass
# Sort the input array and compare if the current value it's the same as the previous one
# Time complexity: O(n*log(n)), Space complexity: O(1)
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate_sort(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
