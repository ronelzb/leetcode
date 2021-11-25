# https://leetcode.com/problems/maximum-subarray/
# tags: #array, #divide_and_conquer, #dp
#
# Solution 1: Dynamic Programming
# Similar to Solution 1, in this case check at each i the max value between current number and the rolling sum
# Then check the if this new max surpasses global max
# Time complexity: O(n), Space complexity: O(1)
#
# Solution 2: Divide and Conquer
# The Divide-and-Conquer algorithm breaks nums into two halves and find the maximum sub array sum in them recursively.
# To handle the case that the maximum sub array spans the two halves we use a linear algorithm:
# Starting from the middle element and move to both ends (left and right ends), record the maximum sum we have seen.
# The maximum sum is finally equal to the middle element plus the maximum sum of moving leftwards and
# the maximum sum of moving rightwards.
# Time complexity: O(n*log(n)), Space complexity: O(n)
from typing import List


class Solution:
    def max_sub_array_dp(self, nums: List[int]) -> int:
        current_max, new_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            new_max = max(nums[i], new_max + nums[i])
            current_max = max(current_max, new_max)

        return current_max

    def max_sub_array_divide_and_conquer(self, nums: List[int], left=0, right=None) -> int:
        if right is None:
            right = len(nums) - 1

        if left == right:
            return nums[left]

        middle = (left + right) // 2

        def _max_crossing_sum(nums, left, middle, right):
            current = 0
            max_left = float("-inf")

            for i in range(middle, left - 1, -1):
                current += nums[i]
                if current > max_left:
                    max_left = current

            current = 0
            max_right = float("-inf")
            for i in range(middle + 1, right + 1):
                current += nums[i]
                if current > max_right:
                    max_right = current

            return max(max_left, max_right, max_left + max_right)

        return max(self.max_sub_array_divide_and_conquer(nums, left, middle),
                   self.max_sub_array_divide_and_conquer(nums, middle + 1, right),
                   _max_crossing_sum(nums, left, middle, right))


if __name__ == "__main__":
    sol = Solution()

    print(sol.max_sub_array_divide_and_conquer([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # [4,-1,2,1] = 6
    print(sol.max_sub_array_divide_and_conquer([5, 4, -1, 7, 8]))  # [5,4,-1,7,8] = 23
