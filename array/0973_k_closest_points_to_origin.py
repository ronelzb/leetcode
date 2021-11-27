# https://leetcode.com/problems/k-closest-points-to-origin/
# tags: #array, #divide_and_conquer, #heap, #math, #quickselect, #sorting
#
# Solution 1: Python built-in heap
# Time complexity: O(n + k*log(n)), Space complexity O(n)
#
# Solution 2: Max-heap
# minheap: when pop, we will get the smallest value. In this problem, is the shortest
# maxheap: when pop, we will get the largest value. In this problem, is the longest.
# As we need to keep the k-smallest values then we need to implement a max-heap
# Time complexity: O(n*log(k) + k) => O(n*log(k)), Space complexity O(k)
#
# Solution 3: Quick select
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/221532/C%2B%2B-STL-quickselect-priority_queue-and-multiset
# Time complexity: O(n), Space complexity O(k)
import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(x ** 2 + y ** 2), x, y) for x, y in points]
        heapq.heapify(distances)
        return [[x, y] for d, x, y in heapq.nsmallest(k, distances)]

    def kClosest_heap2(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            if len(heap) == k:
                heapq.heappushpop(heap, (-distance, x, y))
            else:
                heapq.heappush(heap, (-distance, x, y))

        return [[x, y] for d, x, y in heap]


if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest_heap2(points=[[1, 3], [-2, 2]], k=1))  # [[-2,2]]
    print(sol.kClosest_heap2(points=[[3, 3], [5, -1], [-2, 4]], k=2))  # [[3,3],[-2,4]]
