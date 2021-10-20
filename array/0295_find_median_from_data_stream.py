# https://leetcode.com/problems/find-median-from-data-stream/
# tags: #facebook, #heap, #sorting, #two_pointers
#
# Solution 1: Sorting -> Built-in Sorting
# Sort Insert any incoming number using binary search
# Find the median based on the odd/even half logic
# Time complexity: O(log(n)), Space complexity: O(n)
#
# Solution 2: Two heap
# Make two heaps one that stores the largest element found and the other the smallest
# Then, at insertion time pushpop the input num and directly insert the popped negative element into smallest
# In order to keep both heaps consistent check if largest length is less than smallest and pass the residual to largest
# To find the median check if both heaps length are the same if not then get largest peek.
# Time complexity: O(log(n)), Space complexity: O(n)
import bisect
from heapq import heappush, heappushpop, heappop


class MedianFinder:
    def __init__(self):
        self.nums = []
        self.n = 0

    def addNum(self, num: int) -> None:
        left, right = 0, self.n - 1
        while left <= right:
            middle = (left + right) // 2

            if self.nums[middle] < num:
                left = middle + 1
            else:
                right = middle - 1

        self.nums.insert(left, num)
        self.n += 1

    def addNum_bisect(self, num: int) -> None:
        bisect.insort(self.nums, num)
        self.n += 1

    def findMedian(self) -> float:
        half = self.n // 2
        if self.n % 2 == 0:  # even
            return (self.nums[half - 1] + self.nums[half]) / 2
        else:  # odd
            return self.nums[half]


class MedianFinderHeaps:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(6)
    mf.addNum(5)
    mf.addNum(3)
    print(mf.findMedian())
    mf.addNum(4)
    print(mf.findMedian())
    mf.addNum(7)
    print(mf.findMedian())
