# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# tags: #array, #two_pointers, #sorting
#
# Solution: Queue + Two pointers
# Per @clarencechee solution:
# The question boils down to understanding that if we look at the magnitude of the elements in the array A,
# both ends "slide down" and converge towards the center of the array.
# With that understanding, we can use two pointers, one at each end, to iteratively collect the larger square to a list
# Time complexity: O(n), Space complexity O(n)
#
# Solution 2: No queue
# Add the larger square from the back of the list, denoted by the index r - l.
# Time complexity: O(n), Space complexity O(1)
from collections import deque
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = deque()
        left, right = 0, len(nums) - 1

        while left <= right:
            start, end = abs(nums[left]), abs(nums[right])
            if start > end:
                res.appendleft(start ** 2)
                left += 1
            else:
                res.appendleft(end ** 2)
                right -= 1

        return list(res)

    def sortedSquares_pointers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1

        while left <= right:
            start, end = abs(nums[left]), abs(nums[right])
            if start > end:
                res[right - left] = start ** 2
                left += 1
            else:
                res[right - left] = end ** 2
                right -= 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedSquares_pointers(nums=[-4, -1, 0, 3, 10]))  # [0,1,9,16,100]
