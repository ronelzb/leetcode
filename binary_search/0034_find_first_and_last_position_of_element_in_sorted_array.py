# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# tags: #array, #binary_search
#
# Time complexity goal suggests to implement binary search.
# However because we want the range, we need to use modified binary search, we can do the follow:
# 1. When the nums[mid] is too small, the range starts on the right of mid, so lo = mid + 1.
# 2. For the right boundary, we can merge the the other two conditions into one: right = middle
#
# Eventually, we can optimize our code when finding the result's right boundary (range),
# instead of searching target, we can search target + 1.
# Then deduct 1 from the result to get the correct position of right boundary.
#
# Time complexity: 2*log(n) => log(n), Space complexity: 0(1)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        n = len(nums)
        if n == 0:
            return result

        left = self.search(nums, 0, n, target)
        if left >= n or nums[left] != target:
            return result

        result[0] = left
        result[1] = self.search(nums, left, n, target + 1) - 1

        return result

    def search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3, 4]
    print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=15))  # [-1, -1]
    print(sol.searchRange(nums=[1], target=1))  # [0, 0]
    print(sol.searchRange(nums=[2, 2], target=2))  # [0, 1]
