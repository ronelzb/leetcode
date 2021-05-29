# https://leetcode.com/problems/find-median-from-data-stream/
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
