# https://leetcode.com/problems/missing-number/
# tags: #array, #blind_75_must_do, #hash_table, #math, #top_interview_questions, #sorting
#
# Solution 1: One pass
# Add up the differences between the current index number and the index itself,
# eventually subtract it from the length of the array, we can get the missing number from which the difference occurs
# Time complexity: O(n), Space complexity: O(1)
#
# Solution 2: XOR
# A number XOR itself will become 0, any number XOR with 0 will stay unchanged.
# So if every number from 1...n XOR with itself except the missing number, the result will be the missing number.
# Time complexity: O(n), Space complexity: O(1)
#
# Solution 3: Binary Search
# Sort the array and simply validate that middle index is equal to the middle number
# Time complexity: O(n*log(n)), Space complexity: O(1)
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        diff = 0

        for i, num in enumerate(nums):
            diff += num - i

        return len(nums) - diff

    def missingNumber_xor(self, nums: List[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i
            res ^= num
        return res

    def missingNumber_bs(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > middle:
                right = middle - 1
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    sol = Solution()

    assert sol.missingNumber_bs(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert sol.missingNumber_bs(nums=[1, 0]) == 2
