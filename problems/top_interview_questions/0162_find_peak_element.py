# https://leetcode.com/problems/find-peak-element/
from typing import List


class Solution:
    # https://leetcode.com/problems/find-peak-element/discuss/1290642/intuition-behind-conditions-complete-explanation-diagram-binary-search
    # Using binary search, there is three possible cases at each iteration:
    # Case 1 : mid lies on the right of our result peak ( Observation : Our peak element search space is left side )
    # Case 2 : mid is equal to the peak element ( Observation : mid element is greater than its neighbors )
    # Case 3 : mid lies on the left. ( Observation : Our peak element search space is right side )
    # Time complexity: O(log(n)), Space complexity: O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle - 1] < nums[middle] > nums[middle + 1]:
                return middle
            elif nums[middle] < nums[middle + 1]:
                left = middle
            else:  # nums[middle] < nums[middle - 1]
                right = middle

        return -1


if __name__ == "__main__":
    sol = Solution()

    assert sol.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]) == 1 or 5
