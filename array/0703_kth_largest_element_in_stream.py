# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# tags: #bst, #design, #heap, #must_do_easy_questions, #tree
#
# Solution: Heap
# A min-heap can add and pop the element in log(n) time which is more optimized
# Our heap should be k size because we need to return kth-largest element
# We can get min value at O(1)
# Time complexity: constructor=O((n-k)*log(n)), add=O(log(k))
# Space complexity: O(n)
from heapq import heapify, heappop, heappush, heappushpop
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        heapify(self.nums)

        while len(self.nums) > k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        else:
            heappushpop(self.nums, val)

        return self.nums[0]


if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8
