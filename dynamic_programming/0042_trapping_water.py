# https://leetcode.com/problems/trapping-rain-water/
# tags: #array, #dp, #stack, #two_pointers
#
# Brute Force approach:
# For each element in the array, we find the maximum level of water it can trap after the rain,
# which is equal to the minimum of maximum height of bars on both the sides minus its own height.
# * Iterate the array from left to right:
#   * Initialize max_left = 0 and max_right = 0
#   * Iterate from the current element to the beginning of array updating:
#       * max_left=max(max_left, height[j])
#   * Iterate from the current element to the end of array updating:
#       * max_right=max(max_right, height[j])
#   * Add min(max_left, max_right) − height[i] to ans
# Time complexity: O(n^2), Space complexity: O(1)
#
# Solution 1: Two pointers + Dynamic Programming
# * Find maximum height of bar from the left to right in the array left_maxes
# * Find maximum height of bar from the right to left in the array right_maxes
# * Iterate over the height array and update ans:
#   * Add min(max_left[i], max_right[i]) − height[i] to ans
# Time Complexity: O(3*n) => O(n), Space complexity: O(2*n) => O(n)
#
# Solution 2: Stacks
# We can use stack to keep track of the bars that are bounded by longer bars and hence, may store water.
# We keep a stack and iterate over the array. We add the index of the bar to the stack if bar is smaller
# than or equal to the bar at top of stack, which means that the current bar is bounded by the previous
# bar in the stack.
# If we found a bar longer than that at the top, we are sure that the bar at the top of the stack is bounded
# by the current bar and a previous bar in the stack, hence, we can pop it and add resulting trapped water to ans.
# Time Complexity: O(n), Space complexity: O(n)
#
# Solution 3: Two pointers
# * Initialize left pointer to 0 and right pointer to size-1
# * While left<right, do:
#   * If height[left] is smaller than height[right].
#       * If height[left] ≥ left_max, update left_max
#       * Else add left_max − height[left] to ans
#       * Add 1 to left
#   * Else
#       * If height[right] ≥ right_max, update right_max
#       * Else add right_max − height[right] to ans
#       * Subtract 1 from right
# Time complexity: O(n), Space complexity: O(1)
from collections import deque
from typing import List


class Solution:
    def trap_dp(self, height: List[int]) -> int:
        n = len(height)
        water_trapped = 0
        left_maxes, right_maxes = [0] * n, [0] * n

        left_maxes[0] = height[0]
        for i in range(1, n):
            left_maxes[i] = max(height[i], left_maxes[i - 1])

        right_maxes[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_maxes[i] = max(height[i], right_maxes[i + 1])

        for i in range(1, n):
            water_trapped += min(left_maxes[i], right_maxes[i]) - height[i]

        return water_trapped

    def trap_stack(self, height: List[int]) -> int:
        n = len(height)
        stack = deque()
        water_trapped, i = 0, 0

        while i < n:
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                prev_index = stack.pop()
                if stack:
                    min_height = min(height[stack[-1]], height[i])
                    water_trapped += (min_height - height[prev_index]) * (i - stack[-1] - 1)

        return water_trapped

    def trap_twoPointers(self, height: List[int]) -> int:
        n = len(height)
        water_trapped, left, right = 0, 0, n - 1
        left_max, right_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max: left_max = height[left]
                else: water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max: right_max = height[right]
                else: water_trapped += right_max - height[right]
                right -= 1

        return water_trapped


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap_twoPointers(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(sol.trap_twoPointers(height=[4, 2, 0, 3, 2, 5]))  # 9
