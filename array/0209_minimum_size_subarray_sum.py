# https://leetcode.com/problems/minimum-size-subarray-sum/
# tags: #array, #binary_search, #prefix_sum, #sliding_window
#
# Solution 1: Sliding window technique
# Time complexity: O(n), Space complexity: O(1)
#
# Solution 2: Binary search using a cumulative array as the problem says "sub array sum"
# Time complexity: O(log(n)), Space complexity: O(1)
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = current = 0
        n = len(nums)
        min_length = n + 1

        for i in range(n):
            current += nums[i]

            while current >= target:
                min_length = min(min_length, i - start + 1)
                current -= nums[start]
                start += 1

        return min_length if min_length < n + 1 else 0

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        cums = [nums[0]]
        for i in range(1, n):
            cums.append(cums[-1] + nums[i])

        if cums[-1] < target:
            return 0

        min_length = n
        for i in range(n):
            left, right = i, n - 1

            while left <= right:
                middle = (left + right) // 2
                current = cums[middle] - cums[i] + nums[i]  # replace cum[i] by actual num

                if current >= target:
                    min_length = min(min_length, middle - i + 1)
                    right = middle - 1
                else:
                    left = middle + 1

        return min_length


if __name__ == "__main__":
    sol = Solution()

    assert sol.minSubArrayLen2(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
    assert sol.minSubArrayLen2(target=15, nums=[1, 2, 3, 4, 5]) == 5
    assert sol.minSubArrayLen2(target=11, nums=[1, 2, 3, 4, 5]) == 3
