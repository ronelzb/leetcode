# https://leetcode.com/problems/two-sum/
# tags: #array, #hash_table, #top_interview_questions
#
# Solution: Dictionary
# The key here is that there is always only 1 pair of numbers that satisfies the condition
# To solve this in a single pass we use the equation a = target - b, and since we know the target
# then we can maintain a records of all previous values in the list and comparing the current value
# To keep a record of all previous values we can use a dictionary.
# Time complexity: O(n), Space complexity: O(n)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}

        for i, num in enumerate(nums):
            remaining = target - nums[i]
            if remaining in num_to_idx:
                return [num_to_idx[remaining], i]

            num_to_idx[nums[i]] = i

        return []


if __name__ == "__main__":
    sol = Solution()

    print(sol.twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
    print(sol.twoSum(nums=[3, 2, 4], target=6))  # [1, 2]
