# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List


class Solution:
    # Idea: Use hair and tortoise derived algorithm to find the duplicate
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    sol = Solution()

    assert sol.findDuplicate(nums=[1, 3, 4, 2, 2]) == 2
    assert sol.findDuplicate(nums=[2, 2, 2, 2, 2]) == 2
