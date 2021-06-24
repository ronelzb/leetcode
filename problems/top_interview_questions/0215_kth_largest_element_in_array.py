# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    sol = Solution()

    assert sol.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
