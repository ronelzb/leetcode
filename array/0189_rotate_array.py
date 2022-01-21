# https://leetcode.com/problems/rotate-array/description/
# tags: #array, #math, #two_pointers
#
# Solution 1: 3-step array rotation
# Let's use the example nums = [1,2,3,4,5,6,7], k = 3
# 1. Reverse the entire array. You will get = [7,6,5,4,3,2,1]
# 2. Reverse from 0 to k -1 (7,6,5) = [5,6,7,4,3,2,1]
# 3. Eventually reverse from k to n - 1 (4,3,2,1) = [5,6,7,1,2,3,4]
# Time complexity: O(n), Space complexity: O(1)
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n
        if k == 0: return

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    sol = Solution()
    array = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(array, k=3)
    print(array)  # [5, 6, 7, 1, 2, 3, 4]
