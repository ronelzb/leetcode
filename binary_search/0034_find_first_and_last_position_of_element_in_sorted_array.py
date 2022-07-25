# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# tags: #array, #binary_search
#
# Solution: Binary Search
# Time complexity goal suggests to implement binary search.
# However, because we want the range, we need to use modified binary search, we can do the follow:
# 1. When the nums[mid] is too small, the range starts on the right of mid, so lo = mid + 1.
# 2. For the right boundary, we can merge the other two conditions into one: right = middle
# Eventually, we can optimize our code when finding the result's right boundary (range),
# instead of searching target, we can search target + 1.
# Then deduct 1 from the result to get the correct position of right boundary.
#
# Time complexity: 2*log(n) => log(n), Space complexity: 0(1)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(start: int, end: int, t: int) -> int:
            while start < end:
                middle = (start + end) // 2
                if nums[middle] < t:
                    start = middle + 1
                else:
                    end = middle
            return start

        result = [-1, -1]
        n = len(nums)
        if n == 0:
            return result

        left = search(0, n, target)
        if left >= n or nums[left] != target:
            return result

        result[0] = left
        result[1] = search(left, n, target + 1) - 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3, 4]
    print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=15))  # [-1, -1]
    print(sol.searchRange(nums=[1], target=1))  # [0, 0]
    print(sol.searchRange(nums=[2, 2], target=2))  # [0, 1]
