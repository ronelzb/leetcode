# https://leetcode.com/problems/longest-turbulent-subarray/
# tags: #array, #dp, #sliding_window
#
# Solution 1: Sliding window
# Keep track of the last flip and current flip, if they are the same then reset start_index to i - 1
# Edge case when arr[i] == arr[i - 1], in this case reset start_index to i as last_flip is invalid
# Time Complexity: O(n), Space complexity: O(1)
#
# Solution 2: dp
# We use the counter to track the sub array size.
# Our counter is positive  if we expect '>', and '<' otherwise. For each turn we flip the sign
# Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_length, start_index, last_flip = 1, 0, None
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                start_index = i
                last_flip = None
                continue

            current_flip = 1 if arr[i] > arr[i - 1] else -1
            if last_flip is None or last_flip == current_flip * -1:
                max_length = max(max_length, i - start_index + 1)
            else:
                start_index = i - 1

            last_flip = current_flip

        return max_length

    def maxTurbulenceSize_dp(self, arr: List[int]) -> int:
        max_length, counter = 0, 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                counter = counter + 1 if counter > 0 else 1
            elif arr[i] < arr[i - 1]:
                counter = counter - 1 if counter < 0 else -1
            else:
                counter = 0

            max_length = max(max_length, abs(counter))
            counter *= -1

        return max_length + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxTurbulenceSize_dp(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]))  # 5
    print(sol.maxTurbulenceSize_dp(arr=[4, 8, 12, 16]))  # 2
    print(sol.maxTurbulenceSize_dp(arr=[100]))  # 1
