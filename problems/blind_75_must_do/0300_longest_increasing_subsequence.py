# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    # Solution 1: Using dp to get max_seq for each i. Time complexity: O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    # Solution 2: https://leetcode.com/problems/longest-increasing-subsequence/discuss/173042/Python-solution.
    # Time complexity: O(n*log(n))
    def lengthOfLIS_optimized(self, nums: List[int]) -> int:
        def binary_search(arr, target):
            left = 0
            right = max_seq_length

            while left < right:
                middle = (left + right) // 2

                if arr[middle] == target:
                    return middle
                elif arr[middle] < target:
                    left = middle + 1
                else:
                    right = middle

            return left

        max_seq = [nums[0]]
        max_seq_length = 1
        for i in range(1, len(nums)):
            index = binary_search(max_seq, nums[i])
            if index == max_seq_length:
                max_seq.append(nums[i])
                max_seq_length += 1
            else:
                max_seq[index] = nums[i]

        return max_seq_length


if __name__ == "__main__":
    sol = Solution()

    assert sol.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS_optimized(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4

    assert sol.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS_optimized(nums=[0, 1, 0, 3, 2, 3]) == 4

    assert sol.lengthOfLIS_optimized(nums=[10, 9, 2, 5, 3, 4]) == 3
